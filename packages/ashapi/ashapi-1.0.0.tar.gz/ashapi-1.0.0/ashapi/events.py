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
from typing import Callable, Optional, Any
from enum import Enum

class Events(str, Enum):

    CONNECTED = 'client-connected'
    DISCONNECTED = 'client-disconnected'
    CONNECTION_REFUSED = 'client-connection-refused'

    CONTENT_CREATED = 'content-created'
    CONTENT_DELETED = 'content-deleted'

    SIMULATION_STATE = 'simulation-state'

    AREA = 'area'
    AREA_ORIGIN = 'area-origin'

    ENVIRONMENT_DEPTH = 'environment-depth'
    ENVIRONMENT_TEMPERATURE = 'environment-temperature'
    ENVIRONMENT_TIME = 'environment-time'
    ENVIRONMENT_WIND = 'environment-wind'
    ENVIRONMENT_WAVE = 'environment-wave'
    ENVIRONMENT_CURRENT = 'environment-current'
    ENVIRONMENT_WEATHER_PRESET = 'environment-weather-preset'
    ENVIRONMENT_PRECIPITATIONS = 'environment-precipitations'

    OBJECT_ADD = 'add-object'
    OBJECT_ADD_OFFSET = 'add-object-with-offset'
    OBJECT_ADDED = 'object-added'
    OBJECT_DATA = 'object-data'
    OBJECT_POSITION = 'object-position'
    OBJECT_REMOVE = 'remove-object'
    OBJECT_REMOVED = 'object-removed'

    ROUTE_ADD = 'add-route'
    ROUTE_CHANGE = 'change-route'
    ROUTE = 'route'
    ROUTE_REMOVE = 'remove-route'
    ROUTE_REMOVED = 'route-removed'


class EventBus():

    __slots__ = 'listeners',

    __listeners_container = list


    def __init__(self):
        self.listeners = {}


    def add_listener(self,
                     event_type: str,
                     listener: Callable):
        event_listeners = self.listeners.setdefault(event_type, self.__listeners_container())
        if listener not in event_listeners:
            event_listeners.append(listener)


    def remove_listener(self,
                        event_type: str,
                        listener: Callable):
        try:
            event_listeners = self[event_type]
            if listener in event_listeners:
                event_listeners.remove(listener)
            if not event_listeners:
                del self.listeners[event_type]
            return True
        except KeyError:
            return False


    def emit(self,
             event_type: str,
             payload: Optional[Any] = None):
        acall, acoro, afake = self.__split_listeners(self[event_type])
        if acoro:
            try:
                loop = asyncio.get_running_loop()
                [loop.create_task(coro(payload)) for coro in acoro]
            except RuntimeError:
                pass
        if acall:
            [call(payload) for call in acall]
        if afake:
            raise TypeError("Non-callable listener provided to event bus")



    def emit_tasks(self,
                   event_type: str,
                   payload: Optional[Any]= None):
        try:
            asyncio.get_running_loop()
        except RuntimeError:
            return []
        else:
            _, acoro, _ = self.__split_listeners(self[event_type])
            return [asyncio.create_task(coro(payload)) for coro in acoro]



    async def emit_async(self,
                         event_type: str,
                         payload: Optional[Any] = None):
        acall, acoro, afake = self.__split_listeners(self[event_type])
        if acoro:
            try:
                asyncio.get_running_loop()
            except RuntimeError:
                pass
            else:
                tasks = [asyncio.create_task(coro(payload)) for coro in acoro]
                done, _pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
                for t in done:
                    e = t.exception()
                    if e is not None:
                        raise e
        if acall:
            [call(payload) for call in acall]
        if afake:
            raise TypeError("Non-callable listener provided to event bus")


    @property
    def total_listeners(self):
        return sum(map(len, self.listeners.values()))


    def __getitem__(self, event_type: str):
        try:
            return self.listeners[event_type]
        except KeyError:
            return self.__listeners_container()


    def __split_listeners(self, listeners, _callable = callable, _acoroutine = asyncio.iscoroutinefunction):
        acall, acoro, afake = [], [], []
        if listeners:
            add_call, add_coro, add_fake = acall.append, acoro.append, afake.append
            for entry in listeners:
                if _acoroutine(entry):
                    add_coro(entry)
                elif _callable(entry):
                    add_call(entry)
                else:
                    add_fake(entry)
        return acall, acoro, afake
