import uuid
import asyncio
import traceback
import re
import os
from copy import copy
from typing import Optional, Any, Tuple, Dict, Callable
from dataclasses import dataclass

from termcolor import colored

from .clients.coordinator_client import CoordinatorClient, Handle

from .serialization.task import (
    TaskType,
    LocalFuncCall,
    LocalCompletion,
    func_fullname,
)

from .context import schedule_context, caller_type_context, update_progress_context

from .logging import logger

from .serialization.base import SerializationType


_client = CoordinatorClient()

DEFAULT_WEB_URL = "http://localhost:8080"


def run_workflow_module(workflow_module: Any, *args: Tuple, **kwargs: Dict):
    run_id = uuid.UUID(os.environ["AGENTIC_RUN_ID"])
    history_run_id_env = os.environ.get("AGENTIC_HISTORY_RUN_ID")
    web_url = os.environ.get("AGENTIC_WEB_URL", DEFAULT_WEB_URL)
    history_run_id = uuid.UUID(history_run_id_env) if history_run_id_env else None
    loop = asyncio.new_event_loop()
    assert (
        workflow_module.main
    ), f"Workflow {workflow_module} does not have a main function"

    print(
        f"\nRunning workflow",
    )
    print(
        f"View progress: ",
        end="",
    )
    print(colored(f"{web_url}/r/{run_id}", "white", attrs=["bold"]))

    _, exc = loop.run_until_complete(
        run_workflow(
            run_id=run_id,
            workflow=workflow_module.main,
            args=args,
            kwargs=kwargs,
            history_from_run_id=history_run_id,
            parent_run_id=None,
        )
    )
    if exc:
        print(colored("\nException in workflow:", "red", attrs=["bold"]))
        traceback.print_tb(exc.__traceback__)


async def run_workflow(
    *,
    run_id: uuid.UUID,
    workflow: Callable,
    args: Tuple = (),
    kwargs: Dict = {},
    history_from_run_id: Optional[uuid.UUID] = None,
    parent_run_id: Optional[uuid.UUID] = None,
):
    assert getattr(workflow, "task_type", None) == TaskType.Value(
        "WORKFLOW"
    ), f"Function {func_fullname(workflow)} is not a workflow. Ensure it is wrapped with the workflow decorator."
    main_workflow_scheduled = False
    run_schedule = lambda *args, **kwargs: _schedule(
        run_id=run_id,
        parent_run_id=parent_run_id,
        main_workflow_scheduled=main_workflow_scheduled,
        *args,
        **kwargs,
    )
    schedule_context.set(run_schedule)
    await workflow.schedule(args=args, kwargs=kwargs)
    main_workflow_scheduled = True
    if history_from_run_id:
        await _client.register_new_run_from_existing(history_from_run_id, run_id)
    ret, exc = await _run(run_id, history_from_run_id)
    return ret, exc


async def _schedule(
    *,
    run_id: uuid.UUID,
    parent_run_id: Optional[uuid.UUID],
    main_workflow_scheduled: bool,
    name: str,
    description: str,
    task_type: TaskType,
    function: Callable,
    call_args: Dict,
    serialization: SerializationType,
) -> Handle:
    send_child_run_id = None
    send_parent_run_id = None
    if task_type == TaskType.Value("WORKFLOW"):
        if main_workflow_scheduled:
            # Every subsequent workflow is a child workflow,
            # so assign a child run ID here so we can relate it
            # back to this run.
            send_child_run_id = uuid.uuid4()
        else:
            # Send parent_run_id to simplify linking this workflow back
            # to parent. If we have a parent for this task,
            # then we cannot have a child as well.
            send_parent_run_id = parent_run_id
            assert send_child_run_id is None
    handle = await _client.schedule_task(
        run_id,
        LocalFuncCall(
            name=name,
            description=description,
            task_type=task_type,
            function=function,
            call_args=call_args,
            use_child_run_id=send_child_run_id,
            use_parent_run_id=send_parent_run_id,
            serialization=serialization,
        ),
    )
    return handle


class WorkflowHistoryState:
    def __init__(self, *, history_from_run_id: Optional[uuid.UUID]):
        self._history_valid = True
        self._history_from_run_id = history_from_run_id

    @property
    def history_valid(self):
        return self._history_valid

    @property
    def history_from_run_id(self):
        return self._history_from_run_id

    def invalidate_history(self):
        self._history_valid = False


async def _run(
    run_id: uuid.UUID, history_from_run_id: Optional[uuid.UUID]
) -> Tuple[Optional[Any], Optional[Exception]]:
    history_state = WorkflowHistoryState(
        history_from_run_id=history_from_run_id,
    )
    workflow_result = None
    workflow_exc = None
    finished_event = asyncio.Event()

    def on_main_workflow_done(result: Any):
        nonlocal workflow_result
        workflow_result = result
        finished_event.set()

    def on_main_workflow_failed(exc: Exception):
        nonlocal workflow_exc
        workflow_exc = exc
        finished_event.set()

    while True:
        get_aiotask = asyncio.create_task(_client.get_next_task(run_id))
        finished_aiotask = asyncio.create_task(finished_event.wait())
        done, pending = await asyncio.wait(
            [get_aiotask, finished_aiotask], return_when=asyncio.FIRST_COMPLETED
        )
        for aiotask in pending:
            # Cancel because we can just restart the task on next loop
            aiotask.cancel()
        for aiotask in done:
            if aiotask == get_aiotask:
                res = aiotask.result()
                assert type(res) == tuple
                step, call = res
                on_done = on_main_workflow_done if step == 0 else None
                on_exc = on_main_workflow_failed if step == 0 else None
                asyncio.create_task(
                    _handle_task(
                        run_id,
                        step,
                        call,
                        history_state,
                        on_done=on_done,
                        on_exception=on_exc,
                    )
                )
            elif aiotask == finished_aiotask:
                return workflow_result, workflow_exc


async def _handle_task(
    run_id: uuid.UUID,
    step: int,
    call: LocalFuncCall,
    history_state: WorkflowHistoryState,
    on_done: Optional[Callable],
    on_exception: Optional[Callable],
):
    ret, exc = await _run_function(run_id, step, call, history_state)

    if exc and on_exception:
        on_exception(exc)

    if on_done:
        on_done(ret)


async def _run_function(
    run_id: uuid.UUID,
    step: int,
    call: LocalFuncCall,
    history_state: WorkflowHistoryState,
):
    _log_step(step, call)

    (
        historical_completion,
        historical_child_run_id,
    ) = await _get_historical_data(step, call, history_state)

    await _client.register_task_started(run_id, step)

    async def _update_run_progress(progress: Any):
        await _client.update_task_run_progress(run_id, step, progress)

    update_progress_context.set(_update_run_progress)

    exc, result = await _run_or_use_prev_completion(
        run_id, call, historical_completion, historical_child_run_id, step
    )

    if exc:
        await _client.register_task_failed(run_id, step, exc)
    else:
        await _client.register_task_completed(run_id, step, result, call.serialization)
    return result, exc


async def _run_or_use_prev_completion(
    run_id: uuid.UUID,
    call: LocalFuncCall,
    prev_completion: Optional[LocalCompletion],
    prev_child_run_id: Optional[uuid.UUID],
    step: int,
):
    exc = None
    result = None
    if prev_completion:
        logger.info(colored("\nUsing previous result", "white", attrs=["bold"]))
        result = prev_completion.result
    else:
        try:
            result = await _call_function(run_id, call, step, prev_child_run_id)
        except Exception as e:
            exc = e
    return exc, result


async def _call_function(
    run_id: uuid.UUID,
    call: LocalFuncCall,
    step: int,
    prev_child_run_id: Optional[uuid.UUID],
):
    caller_type_context.set(call.task_type)
    call_args = copy(call.call_args)

    # TODO - This assumes kwargs will always be called kwargs.
    # Need to fix this.
    kwargs = call_args.pop("kwargs", {})
    args = call_args.values()

    if call.task_type == TaskType.Value("WORKFLOW") and step != 0:
        # First step is always the current workflow, every other workflow
        # task is a child workflow
        assert call.use_child_run_id, "Child workflow must have a child run ID"
        result, exc = await run_as_child_workflow(
            parent_run_id=run_id,
            function=call.function,
            args=(),
            kwargs=call_args,
            use_child_run_id=call.use_child_run_id,
            prev_child_run_id=prev_child_run_id,
        )
        if exc:
            raise exc
    else:
        logger.info(colored("\nRunning...\n", "white", attrs=["bold"]))
        # At this point we want to run the inner function directly, otherwise this will just
        # reschedule the function as a new task.
        result = await call.function.run_direct(*args, **kwargs)
    return result


async def _get_historical_data(
    step: int, call: LocalFuncCall, history_state: WorkflowHistoryState
) -> Tuple[Optional[LocalCompletion], Optional[uuid.UUID]]:
    if not history_state.history_from_run_id or not history_state.history_valid:
        return None, None

    (
        prev_completion,
        use_child_run_id,
    ) = await _client.get_matching_historical_data(
        history_state.history_from_run_id, step, call
    )

    if call.task_type == TaskType.Value("WORKFLOW"):
        # Ensure workflows always re-run. We want
        # to step into them to see if anything has changed.
        # However, we don't want to invalidate the history.
        # Return use_child_run_id so we can use it as a history
        # cache for the child workflow that is started.
        return None, use_child_run_id

    if not prev_completion:
        # Invalidate future history as soon as we find a step
        # that has changed
        history_state.invalidate_history()

    return prev_completion, None


async def run_as_child_workflow(
    *,
    parent_run_id: uuid.UUID,
    function: Callable,
    args: Tuple,
    kwargs: Dict,
    use_child_run_id: uuid.UUID,
    prev_child_run_id: Optional[uuid.UUID],
) -> Any:
    return await run_workflow(
        run_id=use_child_run_id,
        workflow=function,
        args=args,
        kwargs=kwargs,
        history_from_run_id=prev_child_run_id,
        parent_run_id=parent_run_id,
    )


def _log_step(step: int, call: LocalFuncCall):
    args = str(call.call_args)
    # Replace repeated spaces with single space.
    # Often args have strings split over multiple lines for readability.
    args = re.sub(r"\s+", " ", args)
    args = args[:100] + "... ]" if len(args) > 100 else args
    logger.info(
        colored(
            f"\nStep {step}. {func_fullname(call.function)}",
            "green",
            attrs=["bold"],
        ),
    )
    logger.info(colored(f"Arguments: {args}", "white"))
