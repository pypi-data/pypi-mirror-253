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

from typing import Optional
from itertools import zip_longest

from . simnettypes import (
    Route as RouteNetType,
    AddRoute,
    ChangeRoute,
    RemoveRoute,
    RouteRemoved
)

from . events import Events
from . proxy import SimDataClient

from . route import Route, RoutePoint


class SimRoutePoint(SimDataClient):

    __slots__ = "_id", "_name", "_index", "_point"

    def __init__(self,
                 id: int,
                 name: str,
                 index: int,
                 p: RoutePoint):
        self._id = id
        self._name = name
        self._index = index
        self._point = p

    def _getattr(self, name, _get=getattr):
        return _get(self._point, name)

    def _setattr(self, name, value, _get=getattr, _set=setattr):
        point = self._point
        v = _get(point, name)
        if v != value:
            _set(point, name, value)
            pdict = point.to_dict(only={name})
            changed = { "index": self._index, "point": pdict }
            self._send(ChangeRoute(self._id, self._name, changed=changed))


    def _set(self, point: RoutePoint, send=False):
        p = self._point
        dirty = set()
        for name in RoutePoint.__slots__:
            value = getattr(point, name)
            if getattr(p, name) != value:
                setattr(p, name, value)
                dirty.add(name)
        if dirty and send:
            pdict = p.to_dict(only=dirty)
            changed = { "index": self._index, "point": pdict }
            self._send(ChangeRoute(self._id, self._name, changed=changed))


class SimRoute(SimDataClient):

    __slots__ = "_id", "_route"

    def __init__(self,
                 route_id: Optional[int] = None):
        self._id = route_id
        self._route = Route()


    @property
    def uid(self):
        return self._id

    @property
    def name(self):
        return self._route.name


    def __len__(self):
        return len(self._route)

    def __getitem__(self, key):
        return self._route[key]

    def __setitem__(self, key, value):
        self[key]._set(value, send=True)

    def __iter__(self):
        yield from self._route.points



    def append(self, point: RoutePoint,
               _proxy = SimRoutePoint):

        n = len(self._route)
        proxy = _proxy(self._id, self._route.name, n, point)._attach(self.client)
        self._route.points.append(proxy)
        pdict = point.to_dict()
        added = { "index": n, "point": pdict }
        self._send(ChangeRoute(self.uid, self.name, added=added))


    def insert(self, index: int, point: RoutePoint,
               _proxy = SimRoutePoint):
        assert index < len(self._route)
        proxy = _proxy(self._id, self._route.name, index, point)._attach(self.client)
        self._route.points.insert(index, proxy)
        for p in self._route.points[index+1:]:
            p._index += 1
        pdict = point.to_dict()
        added = { "index": index, "point": pdict }
        self._send(ChangeRoute(self.uid, self.name, added=added))


    def remove(self, index: int):
        assert index < len(self._route)
        proxy = self._route.points.pop(index)
        proxy._detach()
        for p in self._route.points[index:]:
            p._index -= 1
        self._send(ChangeRoute(self.uid, self.name, removed = { "index": index }))


    def _subscribe(self):
        self.client.subscribe(Events.ROUTE, self.on_route)
        return self

    def _unsubscribe(self):
        if self.client:
            self.client.unsubscribe(Events.ROUTE, self.on_route)
        return self

    #
    # Server routes events handlers
    #

    def on_route(self, data: RouteNetType):
        if self.uid == data.objectid:
            self._receive(data)


    def _receive(self, data: RouteNetType,
                _to_point = RoutePoint.from_dict,
                _proxy = SimRoutePoint):
        _id, _name = data.objectid, data.name
        self._route.name = _name
        points = [_to_point(p) for p in data.points]
        _append = self._route.points.append
        for i, (proxy, p) in enumerate(zip_longest(self._route.points, points)):
            if proxy is None: # new points arrived
                proxy = _proxy(_id, _name, i, p)._attach(self.client)
                _append(proxy)
            elif p is None: # point removed
                for p in self._route.points[i:]:
                    p._detach()
                del self._route.points[i:]
                break
            else: # update proxy, but not send
                proxy._set(p, send=False)


class Routes(SimDataClient):

    __slots__ = "_routes",

    def __init__(self):
        self._routes = {}

    def __len__(self):
        return len(self._routes)

    def _get_by_index(self, index_or_key,
                      _sorted = sorted,
                      _list = list):
        if index_or_key in self._routes:
            return self._routes[index_or_key]
        if self._routes:
            return self._routes[_list(_sorted(self._routes.keys()))[index_or_key]]

    def __getitem__(self, index):
        return self._get_by_index(index)

    def __iter__(self):
        yield from self._routes.values()

    def add(self, name='', points=[]):
        assert len(points) > 1
        self._send(AddRoute(name, points))

    def remove(self, route):
        if route.uid in self._routes:
            self._send(RemoveRoute(route.uid))

    def clear(self):
        for r in self._routes.values():
            r._detach()
        self._routes = {}

    def _subscribe(self):
        self.client.subscribe(Events.ROUTE, self._receive)
        self.client.subscribe(Events.ROUTE_REMOVED, self.on_route_removed)
        return self

    def _unsubscribe(self):
        if self.client:
            self.client.unsubscribe(Events.ROUTE_REMOVED, self.on_route_removed)
            self.client.unsubscribe(Events.ROUTE, self._receive)
        return self

    #
    # Server routes events handlers
    #

    def _receive(self, data: RouteNetType,
                 _route = SimRoute):
        route_id = data.objectid
        if not route_id in self._routes:
            r = _route(route_id = route_id)
            r._attach(self.client)
            r._receive(data)
            self._routes[route_id] = r


    def on_route_removed(self, data: RouteRemoved):
        route_id = data.objectid
        if route_id in self._routes:
            self._routes[route_id]._detach()
            del self._routes[route_id]
