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

from typing import Optional, Union, List, Tuple

from . simnettypes import (
    AddObject,
    ObjectAdded,
    AddObjectWithOffset,
    ObjectData,
    ObjectPosition,
    ObjectPositionOrder,
    ObjectRemoved,
    RemoveObject
)

from . events import Events
from . proxy import SimDataClient

from . geo import GeoPoint, Euler, Vec3, Quat, lla2ecef, ecef2lla, euler2quat, quat2euler
from . pq import PQ

from . area import Area


class SimDevice(SimDataClient):

    __slots__ = "_id", "_path", "_group", "_params", "_devices"

    def __init__(self,
                 object_id: int,
                 object_path: str):
        self._id = object_id
        self._path = object_path
        self._group = ''
        self._params = {}
        self._devices = Devices()

    @property
    def uid(self):
        return self._id

    @property
    def path(self):
        return self._path

    @property
    def tag(self):
        return self._path

    @property
    def values(self):
        ''' Get all device's parameters values in form of dict { parameter_name: parameter_value }'''
        return { pname: pvalue for pname, pvalue in self._params.items() }

    @property
    def orders(self):
        ''' Get all device's orders parameters values in form of dict { parameter_name: parameter_value }'''
        return { pname: pvalue for pname, pvalue in self._params.items() if pname.endswith('_order')}

    @property
    def states(self):
        ''' Get all device's non-orders parameters values in form of dict { parameter_name: parameter_value }'''
        return { pname: pvalue for pname, pvalue in self._params.items() if not pname.endswith('_order') }


    @property
    def devices(self):
        return self._devices

    def _getattr(self, name):
        return self._params.get(name, None)

    def _setattr(self, name, value):
        if value is not None:
            params = self._params
            v = params.get(name, None)
            if v is None or v != value:
                self._send(ObjectData(self._id, group=self._group, path = self._path, values = [{name: value}]))

    def _receive(self, data: ObjectData):
        self._group = data.group
        self._params.update({k: v for entry in data.values for k, v in entry.items()})
        pass

class Devices:

    __slots__ = "_devices", 

    def __init__(self):
        self._devices = {}

    def __len__(self):
        return len(self._devices)

    def find_by(self,
                path: str = '',
                _next = next):
        return _next((d for d in self._devices.values() if d.path == path), None)

    def __getitem__(self, index):
        if isinstance(index, str):
            return self.find_by(path = index)
        return list(self._devices.values())[index]

    def __contains__(self, path):
        return path in self._devices

    def __iter__(self):
        yield from self._devices.items()

    def add(self, device: SimDevice):
        self._devices[device.path] = device

    def remove(self, path: str):
        if path in self._devices:
            d = self._devices[path]
            del self._devices[path]
            return d

    def clear(self):
        for d in self._devices.values():
            d._detach()
        self._devices = {}



class SimObject(SimDataClient):

    __slots__ = "_id", "_code", "_name", "_p", "_q", "_v", "_w", "_group", "_params", "_devices", "_area"

    def __init__(self,
                 object_id: int,
                 object_code: str,
                 object_name: str,
                 area: Area):
        self._id = object_id
        self._code = object_code
        self._name = object_name
        self._p = [0, 0, 0]
        self._q = [0, 0, 0, 1]
        self._v = [0, 0, 0]
        self._w = [0, 0, 0]
        self._group = ''
        self._params = {}
        self._devices = Devices()
        self._area = area


    @property
    def uid(self):
        return self._id

    @property
    def code(self):
        return self._code

    @property
    def name(self):
        return self._name


    @property
    def pos(self) -> Vec3:
        return Vec3(*self._p)

    @property
    def quat(self) -> Quat:
        return Quat(*self._q)


    @property
    def pq(self) -> PQ:
        return PQ(self.pos, self.quat)

    @pq.setter
    def pq(self, value: PQ) -> None:
        msg = ObjectPositionOrder(
            self._id,
            loc = value.p.tuple,
            rot = value.q.tuple,
            v = self._v,
            w = self._w)
        self._send(msg)


    @property
    def geo(self) -> GeoPoint:
        ''' Geolocation (lat, lon, alt) (degrees)'''
        return ecef2lla(self._area.ecef.absp(self.pos))

    @property
    def euler(self) -> Euler:
        ''' Euler angles (heading, pitch, roll) in Local Tangent Plane (degrees)'''
        return quat2euler(self.quat)


    @property
    def linear(self) -> Vec3:
        ''' Linear speed in Local Tangent Plane (m/s) '''
        return Vec3(*self._v)

    @linear.setter
    def linear(self, v: Union[Vec3, List, Tuple]) -> None: # v is 
        msg = ObjectPositionOrder(
            self._id,
            loc = self._p,
            rot = self._q,
            v = v.tuple if isinstance(v, Vec3) else v,
            w = self._w)
        self._send(msg)

    @property
    def angular(self) -> Vec3:
        ''' Angular speed in Local Tangent Plane (rad/s) '''
        return Vec3(*self._w)

    @property
    def sog(self) -> float:
        ''' Speed over ground (m/s) '''
        return self._params["sog"]

    @sog.setter
    def sog(self, value: float) -> None: # value in m/s
        self._setattr("sog_order", value)

    @property
    def cog(self) -> float:
        ''' Course over ground (degrees) '''
        return self._params["cog"]

    @cog.setter
    def cog(self, value: float) -> None: # value in degrees
        self._setattr("cog_order", value)


    @property
    def devices(self):
        return self._devices

    def _getattr(self, name):
        return self._params.get(name, None)

    def _setattr(self, name, value):
        if value is not None:
            params = self._params
            v = params.get(name, None)
            if v is None or v != value:
                self._send(ObjectData(self._id, group=self._group, values = [{name: value}]))

    @property
    def values(self):
        ''' Get all object's parameters values in form of dict { parameter_name: parameter_value }'''
        return { pname: pvalue for pname, pvalue in self._params.items() }

    def _subscribe(self):
        self.client.subscribe(Events.OBJECT_DATA, self.on_object_data)
        self.client.subscribe(Events.OBJECT_POSITION, self.on_object_position)
        return self

    def _unsubscribe(self):
        self._devices.clear()
        if self.client:
            self.client.unsubscribe(Events.OBJECT_POSITION, self.on_object_position)
            self.client.unsubscribe(Events.OBJECT_DATA, self.on_object_data)
        return self

    #
    # Server objects events handlers
    #

    def on_object_data(self, data: ObjectData):
        object_id = data.objectId
        if self._id == object_id:
            path = data.path
            if path: # it is device
                device = self._devices._devices.get(path, None)
                if not device:
                    device = SimDevice(object_id, path)
                    device._attach(self.client)
                    self._devices.add(device)
                device._receive(data)
            else: # it is object
                self._receive(data)


    def on_object_position(self, data: ObjectPosition):
        if self._id == data.objectId:
            self._p = data.globalPose[:]
            self._q = data.globalOrientation[:]
            self._v = data.linearVelocity[:]
            self._w = data.angularVelocity[:]


    def _receive(self, data: ObjectData):
        self._group = data.group
        self._params.update({k: v for entry in data.values for k, v in entry.items()})
        pass


class Objects(SimDataClient):

    __slots__ = "_objects", "_area"

    def __init__(self, area: Area):
        self._objects = {}
        self._area = area

    def __len__(self):
        return len(self._objects)

    def find_by(self,
                id: Optional[int] = None,
                code: str = '',
                name: str = '',
                _next = next):
        if id in self._objects:
            return self._objects[id]
        if self._objects:
            if code:
                return _next((o for o in self._objects.values() if o.code == code), None)
            if name:
                return _next((o for o in self._objects.values() if o.name == name), None)

    def __getitem__(self, index):
        if isinstance(index, str):
            return self.find_by(code = index) or self.find_by(name = index)
        return list(self._objects.values())[index]

    def add(self,
            code: str,
            name: str ='',
            geo: Optional[GeoPoint] = None,
            eul: Optional[Euler] = None,
            p: Optional[Vec3] = None,
            pq: Optional[PQ] = None,
            v: Optional[Vec3] = None,
            w: Optional[Vec3] = None,
            heading: Optional[float] = None,
            pitch: Optional[float] = None,
            roll: Optional[float] = None,
            sog: Optional[float] = None):
        msg = None
        g = geo
        if geo is not None:
            e = eul
            if eul is None:
                e = Euler(heading if heading is not None else 0.0,
                          pitch if pitch is not None else 0.0,
                          roll if roll is not None else 0.0)
            v = v or Vec3()
            w = w or Vec3()
            pqo = self._area.ecef.rel(PQ(*lla2ecef(g, e)))
            msg = AddObject(
                code,
                name,
                loc = pqo.p.tuple,
                rot = pqo.q.tuple,
                v = v.tuple,
                w = w.tuple
            )
            self._send(msg)
        elif p is not None:
            heading = eul.heading if eul is not None else heading
            velocity = v[0] if v is not None else sog
            msg = AddObjectWithOffset(
                code,
                name,
                offset = (p[0], p[1]),
                cog = heading or 0.0,
                sog = velocity or 0.0,
            )
            self._send(msg)
        elif pq is not None:
            q = pq.q
            if eul:
                q = euler2quat(eul)
            if heading is not None or pitch is not None or roll is not None:
                e = Euler(heading if heading is not None else 0.0,
                          pitch if pitch is not None else 0.0,
                          roll if roll is not None else 0.0)
                q = euler2quat(e)
            v = v or Vec3()
            w = w or Vec3()
            msg = AddObject(
                code,
                name,
                loc = pq.p.tuple,
                rot = q.tuple,
                v = v.tuple,
                w = w.tuple
            )
            self._send(msg)
        else:
            raise ValueError("Can't add object, position data is not provided")

    def remove(self, obj):
        if obj.uid in self._objects:
            self._send(RemoveObject(obj.uid))

    def clear(self):
        for obj in self._objects.values():
            obj._detach()
        self._objects = {}

    def _subscribe(self):
        self.client.subscribe(Events.OBJECT_ADDED, self.on_object_added)
        self.client.subscribe(Events.OBJECT_REMOVED, self.on_object_removed)
        return self

    def _unsubscribe(self):
        if self.client:
            self.client.unsubscribe(Events.OBJECT_REMOVED, self.on_object_removed)
            self.client.unsubscribe(Events.OBJECT_ADDED, self.on_object_added)
        return self

    #
    # Server objects events handlers
    #

    def on_object_added(self, added: ObjectAdded,
                       _object = SimObject):
        object_id = added.objectId
        if object_id not in self._objects:
            obj = _object(object_id, added.code, added.name, self._area)
            obj._attach(self.client)
            self._objects[object_id] = obj


    def on_object_removed(self, data: ObjectRemoved):
        object_id = data.objectId
        if object_id in self._objects:
            self._objects[object_id]._detach()
            del self._objects[object_id]
