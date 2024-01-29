from typing import Any, Tuple, Optional
import asyncio
import uuid
from dataclasses import dataclass

import backoff

from grpc.aio import AioRpcError

from agentic.proto import coordinator_pb2_grpc, coordinator_pb2

from .grpc_channel import get_channel

from ..serialization.task import (
    LocalFuncCall,
    LocalCompletion,
    serialize_func_call_as_task,
    deserialize_task,
    serialize_task_result,
    calls_match,
    serialize_exception,
)

from ..serialization.base import (
    SerializationType,
    serialize_any_as_json_wrapper,
    deserialize_any,
)


DEFAULT_TIMEOUT = 30

_handles = {}


class Handle:
    def __init__(self, *, run_id: uuid.UUID, step: int):
        self.run_id = run_id
        self.step = step
        self._result = None
        self._exception = None
        self._finished_event = asyncio.Event()

    def set_result(self, result: Any):
        self._result = result
        self._finished_event.set()

    def set_exception(self, exception: Exception):
        self._exception = exception
        self._finished_event.set()

    async def wait(self):
        await self._finished_event.wait()
        if self._exception:
            raise self._exception
        return self._result


class CoordinatorClient:
    @property
    async def _stub(self) -> coordinator_pb2_grpc.CoordinatorServiceStub:
        channel = await get_channel()
        stub = coordinator_pb2_grpc.CoordinatorServiceStub(channel)
        return stub

    def _add_handle(self, handle: Handle):
        _handles[(handle.run_id, handle.step)] = handle

    def _get_handle(self, run_id: uuid.UUID, step: int):
        handle = _handles.get(
            (
                run_id,
                step,
            )
        )
        assert handle, f"Handle not found for {run_id} {step}"
        return handle

    async def schedule_task(
        self,
        run_id: uuid.UUID,
        call: LocalFuncCall,
    ) -> Handle:
        assert not (
            call.use_parent_run_id and call.use_child_run_id
        ), "Must specify only one of parent_run_id or child_run_id"
        task = serialize_func_call_as_task(call)
        parent_run_id_str = (
            str(call.use_parent_run_id) if call.use_parent_run_id else None
        )
        child_run_id_str = str(call.use_child_run_id) if call.use_child_run_id else None
        req = coordinator_pb2.ScheduleTaskRequest(
            run_id=str(run_id),
            parent_run_id=parent_run_id_str,
            child_run_id=child_run_id_str,
            task=task,
        )
        stub = await self._stub
        res = await stub.ScheduleTask(req, timeout=DEFAULT_TIMEOUT)
        handle = Handle(run_id=run_id, step=res.step)
        self._add_handle(handle)
        return handle

    @backoff.on_exception(
        backoff.constant,
        (AioRpcError),
        max_tries=3,
        logger=None,
    )
    async def get_next_task(self, run_id: uuid.UUID) -> Tuple[int, LocalFuncCall]:
        stub = await self._stub
        res = await stub.GetNextTask(
            coordinator_pb2.GetNextTaskRequest(run_id=str(run_id))
        )
        call = deserialize_task(res.task, res.use_child_run_id)
        return res.step, call

    async def register_task_started(self, run_id: uuid.UUID, step: int):
        stub = await self._stub
        await stub.RegisterTaskStarted(
            coordinator_pb2.RegisterTaskStartedRequest(run_id=str(run_id), step=step),
            timeout=DEFAULT_TIMEOUT,
        )

    async def register_task_completed(
        self,
        run_id: uuid.UUID,
        step: int,
        result: Any,
        serialization: SerializationType,
    ):
        res = serialize_task_result(result, serialization=serialization)
        stub = await self._stub
        await stub.RegisterTaskCompleted(
            coordinator_pb2.RegisterTaskCompletedRequest(
                run_id=str(run_id), step=step, result=res
            ),
            timeout=DEFAULT_TIMEOUT,
        )
        # TODO — Handle result should be set by the coordinator, not
        # here.
        self._get_handle(run_id, step).set_result(result)

    async def register_task_failed(
        self, run_id: uuid.UUID, step: int, exception: Exception
    ):
        exc = serialize_exception(exception)
        stub = await self._stub
        await stub.RegisterTaskFailed(
            coordinator_pb2.RegisterTaskFailedRequest(
                run_id=str(run_id), step=step, exception=exc
            ),
            timeout=DEFAULT_TIMEOUT,
        )
        self._get_handle(run_id, step).set_exception(exception)

    @backoff.on_exception(
        backoff.constant,
        (AioRpcError),
        max_tries=3,
    )
    async def update_task_run_progress(
        self, run_id: uuid.UUID, step: int, progress: Any
    ):
        stub = await self._stub
        await stub.UpdateTaskRunProgress(
            coordinator_pb2.UpdateTaskRunProgressRequest(
                run_id=str(run_id),
                step=step,
                progress=serialize_any_as_json_wrapper(progress),
            ),
            timeout=DEFAULT_TIMEOUT,
        )

    async def register_new_run_from_existing(
        self, existing_run_id: uuid.UUID, new_run_id: uuid.UUID
    ):
        stub = await self._stub
        await stub.RegisterNewRunFromExisting(
            coordinator_pb2.RegisterNewRunFromExistingRequest(
                new_run_id=str(new_run_id), existing_run_id=str(existing_run_id)
            ),
            timeout=DEFAULT_TIMEOUT,
        )

    async def get_matching_historical_data(
        self, run_id: uuid.UUID, step: int, call: LocalFuncCall
    ) -> Tuple[Optional[LocalCompletion], Optional[uuid.UUID]]:
        stub = await self._stub
        res = await stub.QueryScheduledTask(
            coordinator_pb2.QueryScheduledTaskRequest(
                run_id=str(run_id),
                step=step,
            ),
            timeout=DEFAULT_TIMEOUT,
        )
        if not res.HasField("task"):
            return None, None

        if not calls_match(call, res.task):
            return None, None

        completion = None
        if not res.HasField("completion"):
            return None, None
        # Ignore serialization type as it should not be needed
        prev_result, _ = deserialize_any(res.completion.result)
        completion = LocalCompletion(result=prev_result)
        return completion, res.child_run_id
