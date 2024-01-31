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

import inspect
import sys

from typing import Optional


class SimRequest:

    resource = ''
    method = ''

    __slots__ = ['params']

    def __init__(self):
        self.params = {}


#
# Simulation State
#
class SimulationState(SimRequest):

    method = 'PATCH'
    resource = '/simulation/state'

    __slots__ = []

    def __init__(self,
                 command: str,
                 accel: Optional[float] = None):
        super().__init__()
        self.params = { 'command': command }
        if accel is not None:
            self.params['accel'] = accel

    @classmethod
    def run(cls, accel: Optional[float] = None):
        return cls('run', accel)

    @classmethod
    def accel(cls, accel = float):
        return cls('accel', accel)

    @classmethod
    def maxaccel(cls):
        return cls('maxaccel')

    @classmethod
    def pause(cls):
        return cls('pause')

    @classmethod
    def step(cls):
        return cls('step')


#
# Scene
#

class SceneClear(SimRequest):

    method = 'POST'
    resource = '/scene/clear'

    __slots__ = []


class SceneNew(SimRequest):

    method = 'POST'
    resource = '/scene/new'

    __slots__ = []

    def __init__(self, path: str = None):
        super().__init__()
        if path is not None:
            self.params = { 'path': path }


class SceneOpen(SimRequest):

    method = 'POST'
    resource = '/scene/open'

    __slots__ = []

    def __init__(self, path: str):
        self.params = { 'path': path }


class SceneSave(SimRequest):

    method = 'POST'
    resource = '/scene/save'

    __slots__ = []

    def __init__(self, path: str):
        self.params = { 'path': path }



#
# Recording
#

class RecordingOpen(SimRequest):

    method = 'POST'
    resource = '/recording/open'

    __slots__ = []

    def __init__(self, path: str):
        self.params = { 'path': path }


class RecordingSave(SimRequest):

    method = 'POST'
    resource = '/recording/save'

    __slots__ = []

    def __init__(self, path: str):
        self.params = { 'path': path }


class RecordingSeek(SimRequest):

    method = 'POST'
    resource = '/recording/seek'

    __slots__ = []

    def __init__(self, time: float):
        self.params = { 'time': time }


class RecordingSwitch(SimRequest):

    method = 'POST'
    resource = '/recording/switch'

    __slots__ = []


#
# Data
#

class Exercises(SimRequest):

    method = 'GET'
    resource = '/exercises'

    __slots__ = []


class Recordings(SimRequest):

    method = 'GET'
    resource = '/recordings'

    __slots__ = []


class Models(SimRequest):

    method = 'GET'
    resource = '/models'

    __slots__ = []


class ModelImage(SimRequest):

    method = 'GET'
    resource = '/models/image'

    __slots__ = []

    def __init__(self, code: str):
        self.params = { 'code': code }


class Areas(SimRequest):

    method = 'GET'
    resource = '/areas'

    __slots__ = []


class AreaImage(SimRequest):

    method = 'GET'
    resource = '/areas/image'

    __slots__ = []

    def __init__(self, code: str):
        self.params = { 'code': code }


class AreaMap(SimRequest):

    method = 'GET'
    resource = '/area/map'

    __slots__ = []

    def __init__(self, code: str, map_name: str):
        self.params = { 'code': code, 'map': map_name}


#
# Generate REQUESTS map { resource : SimRequestType }
#

REQUESTS = {cls.resource : cls \
            for _, cls in inspect.getmembers(sys.modules[__name__], lambda x: inspect.isclass(x) and (x.__module__ == __name__)) \
            if issubclass(cls, SimRequest) and cls != SimRequest}
