'''
Copyright (c) 2024 SimTech LLC.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
'''

import asyncio

from time import perf_counter
from typing import Callable, Optional


class Timer:

    __slots__ = "t0", "t1", "clock"

    def __init__(self, 
                 clock: Callable = perf_counter):
        self.clock = clock
        self.reset()

    def reset(self):
        self.t0 = self.clock()
        self.t1 = self.t0

    def span(self):
        self.t1 = self.clock()
        return self.t1 - self.t0


    # def copy(self):
    #     return Timer(self.clock)


async def wait_until(t, span, _sleep = asyncio.sleep):
    _t = span()
    while _t < t:
        await _sleep(0.01)
        _t = span()


def done_callback_scheduler(task):
    def schedule(foo, *args):
        if asyncio.iscoroutinefunction(foo):
            task.add_done_callback(lambda t: asyncio.get_running_loop().create_task(foo(*args)))
        elif callable(foo):
            task.add_done_callback(lambda t: foo(*args))
        return task
    return schedule


def call_at(
        t: Optional[float] = None, # schedule a call after t seconds of timer clock
        timer: Timer = Timer()
        ) -> Callable:
    task = asyncio.get_running_loop().create_task(wait_until(t, timer.span))
    return done_callback_scheduler(task)


class keepfunc:
    '''
    Class to supply callable, which memoize function to call later.
    '''

    __slots__ = "func", "args"

    def __call__(self, func, *args):
        if not callable(func):
            raise TypeError("the first argument must be callable")
        self.func = func
        self.args = args
