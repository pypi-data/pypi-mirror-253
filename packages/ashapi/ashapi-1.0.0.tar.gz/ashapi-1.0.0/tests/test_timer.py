import pytest
import asyncio

from time import time, sleep

from ashapi.timer import Timer, call_at


def test_timer_default(capsys):

    with capsys.disabled():

        tm = Timer()
        # print(f"test_timer_default: t0 = {tm.span()}")

        sleep(0.1)

        # print(f"test_timer_default: t1 = {tm.span()}")

        t = tm.span()

        # print(f"test_timer_default: t1 = {t}")

        assert t >= 0.09

        sleep(0.1)

        # print(f"test_timer_default: t2 = {tm.span()}")

        t = tm.span()

        # print(f"test_timer_default: t2 = {t}")

        assert t >= 0.18


@pytest.mark.asyncio
async def test_timer_call_at(capsys):

    with capsys.disabled():

        tm = Timer()
        # t = tm.span()
        # print(f"test_timer_call_at: t0 = {t} = {tm.clock()} - {tm.t0}")

        # tm1 = Timer(asyncio.get_event_loop().time)
        # t = tm1.span()
        # print(f"test_timer_call_at: t0[1] = {t} = {tm1.clock()} - {tm1.t0}")

        param = {}

        def scheduled(param, tm):
            # t = tm.span()
            # print(f"test_timer_call_at.sheduled: t0 = {t} = {tm.clock()} - {tm.t0}")
            # t = tm1.span()
            # print(f"test_timer_call_at.sheduled: t0[1] = {t} = {tm1.clock()} - {tm1.t0}")
            t = tm.span()
            param['t'] = t
            # print(f"test_timer_call_at.sheduled: t1 = {t} = {tm.clock()} - {tm.t0}")
            # t = tm1.span()
            # print(f"test_timer_call_at.sheduled: t1[1] = {t} = {tm1.clock()} - {tm1.t0}")

        # t = tm.span()
        # print(f"test_timer_call_at: t1 = {t} = {tm.clock()} - {tm.t0}")

        call_at(0.5, tm)(scheduled, param, tm)

        # t = tm.span()
        # print(f"test_timer_call_at: t2 = {t} = {tm.clock()} - {tm.t0}")

        await asyncio.sleep(1.0)

        # t = tm.span()
        # print(f"test_timer_call_at: t3 = {t} = {tm.clock()} - {tm.t0}")

        assert param['t'] >= 0.5
        assert param['t'] < 1.0

