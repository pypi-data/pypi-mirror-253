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

import sys
import inspect
import json

from typing import Dict, List, Optional


class NetType:

    type = ''

    __slots__ = "data",

    def __init__(self):
        self.data = {}

    def __getattr__(self, name):
        data = object.__getattribute__(self, "data")
        if name == "data":
            return data
        return data[name] if name in data else None

    def __setattr__(self, name, value):
        if name == "data":
            object.__setattr__(self, "data", value)
            return
        self.data[name] = value

    @classmethod
    def from_dict(cls, d):
        obj = cls()
        obj.data = d
        return obj

    def to_jstr(self,
                _dumps = json.dumps):
        jsdict = { key : value for key, value in self.data.items() if value is not None}
        jstr = _dumps({'type':self.type, 'json': jsdict}, separators=(',', ':'))
        return jstr

    #
    # For testing and debug
    #

    def __eq__(self, other):
        cls = type(self)
        if isinstance(other, cls):
            return self.data == other.data
        return False

    def __str__(self):
        return self.to_jstr()


class ContentCreated(NetType):
    type = 'content-created'
    __slots__ = [] # "path",

    def __init__(self,
                 path: str = ''):
        self.data = { 'path': path }


class ContentDeleted(NetType):
    type = 'content-deleted'
    __slots__ = []


class AreaOrigin(NetType):
    type = 'area-origin'
    __slots__ = [] # "lat", "lon"

    def __init__(self,
                 lat: float = 0.0,
                 lon: float = 0.0):
        self.data = { 'lat': lat, 'lon': lon }


class AreaOriginOrder(AreaOrigin):
    type = 'area-origin-order'
    __slots__ = [] # "lat", "lon"


class Area(NetType):
    type = 'area'
    __slots__ = [] # "name", "origo", "meshes", "maps"

    def __init__(self,
                 name: str = "",
                 origo: list = [0.0, 0.0],
                 meshes: list = [],
                 maps: list = []):
        self.data = { 'name': name, 'origo': origo, 'meshes': meshes, 'maps': maps }


class AreaOrder(NetType):
    type = 'area-order'
    __slots__ = [] # "name", "title", "description", "origo", "meshes", "maps"

    def __init__(self,
                 name: str = "",
                 title: Optional[str] = None,
                 description: Optional[List] = None,
                 origo: list = [0.0, 0.0],
                 meshes: list = [],
                 maps: list = []):
        self.data = { 'name': name, 'title': title, 'description': description, 'origo': origo, 'meshes': meshes, 'maps': maps }


class EnvironmentDepth(NetType):
    type = 'environment-depth'
    __slots__ = [] # "depth",

    def __init__(self,
                 depth: float = 0):
        self.data = { 'depth': depth }

class EnvironmentDepthOrder(EnvironmentDepth):
    type = 'environment-depth-order'
    __slots__ = [] # "depth",


class EnvironmentTemperature(NetType):
    type = 'environment-temperature'
    __slots__ = [] # "air", "water"

    def __init__(self,
                 air: float = 0,
                 water: float = 0):
        self.data = { 'air': air, 'water': water }


class EnvironmentTemperatureOrder(EnvironmentTemperature):
    type = 'environment-temperature-order'
    __slots__ = [] # "air", "water"


class EnvironmentTime(NetType):
    type = 'environment-time'
    __slots__ = [] # "time",

    def __init__(self,
                 time: float = 0):
        self.data = { 'time' : time }


class EnvironmentTimeOrder(EnvironmentTime):
    type = 'environment-time-order'
    __slots__ = [] # "time",


class EnvironmentWind(NetType):
    type = 'environment-wind'
    __slots__ = [] # "direction_from", "speed"

    def __init__(self,
                 direction_from: float = 0,
                 speed: float = 0):
        self.data = { 'direction_from': direction_from, 'speed': speed }


class EnvironmentWindOrder(EnvironmentWind):
    type = 'environment-wind-order'
    __slots__ = [] # "direction_from", "speed"


class EnvironmentCurrent(NetType):
    type = 'environment-current'
    __slots__ = [] # "direction_to", "speed"

    def __init__(self,
                 direction_to: float = 0,
                 speed: float = 0):
        self.data = { 'direction_to': direction_to, 'speed': speed }


class EnvironmentCurrentOrder(EnvironmentCurrent):
    type = 'environment-current-order'
    __slots__ = [] # "direction_to", "speed"


class EnvironmentWave(NetType):
    type = 'environment-wave'
    __slots__ = [] # "direction_to", "wind_speed", "typical_height", "typical_length", "direction_spread", "number_of_frequencies", "number_of_directions"

    def __init__(self,
                 direction_to: float = 0,
                 wind_speed: float = 0,
                 typical_height: float = 0,
                 typical_length: float = 0,
                 direction_spread: float = 0,
                 number_of_frequencies: int = 0,
                 number_of_directions: int = 0):
        self.data = {
            'direction_to': direction_to,
            'wind_speed': wind_speed,
            'typical_height': typical_height,
            'typical_length': typical_length,
            'direction_spread': direction_spread,
            'number_of_frequencies': number_of_frequencies,
            'number_of_directions': number_of_directions
        }

class EnvironmentWaveOrder(EnvironmentWave):
    type = 'environment-wave-order'
    __slots__ = [] # "direction_to", "wind_speed", "typical_height", "direction_spread", "number_of_frequencies", "number_of_directions"


class EnvironmentWeatherPreset(NetType):
    type = 'environment-weather-preset'
    __slots__ = [] # "preset",

    def __init__(self,
                 preset: int = 0):
        self.data = { 'preset': preset }


class EnvironmentPrecipitations(NetType):
    type = 'environment-precipitations'
    __slots__ = [] # "fog", "clouds", "rain", "snow"

    def __init__(self,
                 fog: float = 0,
                 clouds: float = 0,
                 rain: float = 0,
                 snow: float = 0):
        self.data = { 'fog': fog, 'clouds': clouds, 'rain': rain, 'snow': snow }


class EnvironmentPrecipitationsOrder(EnvironmentPrecipitations):
    type = 'environment-precipitations-order'
    __slots__ = [] # "fog", "clouds", "rain", "snow"


class SimulationState(NetType):
    type = 'simulation-state'
    __slots__ = [] # "running", "playback", "recording", "created", "duration", "start", "time", "ticks", "accel", "maxaccel", "realaccel"

    def __init__(self,
                 running: bool = False,
                 playback: bool = False,
                 recording: bool = False,
                 created: bool = False,
                 duration: float = 0.0,
                 start: float = 0.0,
                 time: float = 0.0,
                 ticks: int = 0,
                 accel: float = 1.0,
                 maxaccel: bool = False,
                 realaccel: float = 1.0):
        self.data = {
            'running': running,
            'playback': playback,
            'recording': recording,
            'created': created,
            'duration': duration,
            'start': start,
            'time': time,
            'ticks': ticks, 
            'accel': accel,
            'maxaccel': maxaccel,
            'realaccel': realaccel
        }


class AddObject(NetType):
    type = 'add-object'
    __slots__ =  [] # "code", "name", "globalPose", "globalOrientation", "linearVelocity", "angularVelocity"

    def __init__(self,
                 code: str = "",
                 name: str = "",
                 loc: tuple = (0, 0, 0),
                 rot: tuple = (0, 0, 0, 0),
                 v: tuple = (0, 0, 0),
                 w: tuple = (0, 0, 0)):
        self.data = {
            'code': code,
            'name': name,
            'globalPose': loc,
            'globalOrientation': rot,
            'linearVelocity': v,
            'angularVelocity': w
        }


class AddObjectWithOffset(NetType):
    type = 'add-object-with-offset'
    __slots__ =  [] # "code", "name", "offset", "cog", "sog"

    def __init__(self,
                 code: str = "",
                 name: str = "",
                 offset: tuple = (0, 0),
                 cog: float = 0.0,
                 sog: float = 0.0):
        self.data = {
            'code': code,
            'name': name,
            'offset': offset,
            'cog': cog,
            'sog': sog
        }


class ObjectAdded(NetType):
    type = 'object-added'
    __slots__ = [] # "objectId", "code", "name"

    def __init__(self,
                 id: int = 0,
                 code: str = "",
                 name: str = ""):
        self.data = { 'objectId': id, 'code': code, 'name': name }


class ObjectData(NetType):
    type = 'object-data'
    __slots__ = [] # "objectId", "group", "path", "values"

    def __init__(self,
                 id: int = 0,
                 group: str = "",
                 path: str = "",
                 values: list = []):
        self.data = { 'objectId': id, 'group': group, 'path': path, 'values': values }


class RemoveObject(NetType):
    type = 'remove-object'
    __slots__ = [] # "objectId",

    def __init__(self,
                 id: int = 0):
        self.data = { 'objectId': id }


class ObjectRemoved(NetType):
    type = 'object-removed'
    __slots__ = [] # "objectId",

    def __init__(self,
                 id: int = 0):
        self.data = { 'objectId': id }


class ObjectPosition(NetType):
    type = 'object-position'
    __slots__ = [] # "objectId", "globalPose", "globalOrientation", "linearVelocity", "angularVelocity"

    def __init__(self,
                 id: int = 0,
                 loc: tuple = (0, 0, 0),
                 rot: tuple = (0, 0, 0, 0),
                 v: tuple = (0, 0, 0),
                 w: tuple = (0, 0, 0)):
        self.data = {
            'objectId': id,
            'globalPose': loc,
            'globalOrientation': rot,
            'linearVelocity': v,
            'angularVelocity': w
        }


class ObjectPositionOrder(ObjectPosition):
    type = 'object-positionorder'
    __slots__ = [] # "objectId", "globalPose", "globalOrientation", "linearVelocity", "angularVelocity"


class AddRoute(NetType):
    type = 'add-route'
    __slots__ = [] # "name", "points"

    def __init__(self,
                 name: str = "",
                 points: list = []):
        self.data = { 'name': name, 'points': points }


class ChangeRoute(NetType):
    type = 'change-route'
    __slots__ =  "objectid", "name", "added", "changed", "removed"

    def __init__(self,
                 id: int = 0,
                 name: str = "",
                 added: Optional[Dict] = None,
                 changed: Optional[Dict] = None,
                 removed: Optional[Dict] = None):
        self.data = { 'objectid': id, 'name': name, 'added': added, 'changed': changed, 'removed': removed }


class Route(NetType):
    type = 'route'
    __slots__ =  "objectid", "name", "points"

    def __init__(self,
                 id: int = 0,
                 name: str = "",
                 points: list = []):
        self.data = { 'objectid': id, 'name': name, 'points': points }


class RemoveRoute(NetType):
    type = 'remove-route'
    __slots__ = [] # "objectid",

    def __init__(self,
                 id: int = 0):
        self.data = { 'objectid': id }


class RouteRemoved(NetType):
    type = 'route-removed'
    __slots__ = [] # "objectid",

    def __init__(self,
                 id: int = 0):
        self.data = { 'objectid': id }


#
# Generate NETTYPES map { nettype : NetTypeClass }
#

NETTYPES = {cls.type : cls \
            for _, cls in inspect.getmembers(sys.modules[__name__], lambda x: inspect.isclass(x) and (x.__module__ == __name__)) \
            if issubclass(cls, NetType) and cls != NetType}


def nettypes_factory(msg: str, _types = NETTYPES, _load = json.loads):
    js = _load(msg)
    typo = js['type']
    if typo in _types:
        return _types[typo].from_dict(_load(js['json']))


