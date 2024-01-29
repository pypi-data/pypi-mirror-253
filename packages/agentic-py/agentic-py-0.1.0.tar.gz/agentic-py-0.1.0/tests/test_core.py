import uuid
import asyncio
import pytest

import agentic as ag

from agentic.core.run_workflow import run_workflow


ANSWER = 42


@ag.action()
async def get_result(to_add: int):
    return ANSWER + to_add


@pytest.mark.asyncio
async def test_simple_answer_workflow():
    @ag.workflow()
    async def simple_answer_wf():
        res = await get_result(0)
        return res

    res, _ = await run_workflow(
        run_id=uuid.uuid4(),
        workflow=simple_answer_wf,
    )
    assert res == ANSWER


@pytest.mark.asyncio
async def test_schedule():
    @ag.workflow()
    async def schedule_step_wf(to_add: int):
        handle = await get_result.schedule(args=(to_add,), kwargs={})
        res = await handle.wait()
        return res

    to_add = 2
    res, _ = await run_workflow(
        run_id=uuid.uuid4(),
        workflow=schedule_step_wf,
        args=(to_add,),
    )
    assert res == ANSWER + to_add


@pytest.mark.asyncio
@pytest.mark.skip("Broken by changes to serialization")
async def test_history_from_prev_run():
    cur = 0

    @ag.action()
    async def inc_cur(inc_by: int):
        nonlocal cur
        cur += inc_by
        return cur

    @ag.workflow()
    async def history_wf(inc_by: int):
        return await inc_cur(inc_by)

    initial_run_id = uuid.uuid4()

    res, _ = await run_workflow(run_id=initial_run_id, workflow=history_wf, args=(1,))

    assert res == 1

    # Run again, but this time use the previous run as history.
    # Given workflow has not changed, the result should be the same.
    res, _ = await run_workflow(
        run_id=uuid.uuid4(),
        workflow=history_wf,
        args=(1,),
        history_from_run_id=initial_run_id,
    )

    assert res == 1

    # Change arg, now result should be different
    # as action will be re-run
    res, _ = await run_workflow(
        run_id=uuid.uuid4(),
        workflow=history_wf,
        args=(2,),
        history_from_run_id=initial_run_id,
    )

    assert res == 3


@pytest.mark.asyncio
async def test_concurrent_actions():
    cur = 0

    @ag.action()
    async def inc_concurrent_cur(inc_by: int):
        nonlocal cur
        cur += inc_by
        return cur

    @ag.workflow()
    async def concurrent_actions_wf():
        await asyncio.gather(
            inc_concurrent_cur(1), inc_concurrent_cur(2), inc_concurrent_cur(3)
        )
        return cur

    res, _ = await run_workflow(
        run_id=uuid.uuid4(),
        workflow=concurrent_actions_wf,
        args=(),
    )

    assert res == 6


@pytest.mark.asyncio
async def test_recover_workflow_run():
    # TODO - Implement wf recovery
    pass


@pytest.mark.asyncio
async def test_child_wf():
    # TODO - Complete test
    pass
