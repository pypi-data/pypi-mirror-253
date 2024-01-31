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

from typing import Union, List, Tuple, Optional

from enum import IntEnum
from collections import namedtuple

import json

from . geo import GeoPoint, dd2nmea, nmea2dd


class PointType(IntEnum):
    STOP = 0
    PASS = 1


WP = namedtuple("WP", "name, lat, ns, lon, ew, radius, velocity, heading, type")


class RoutePoint:

    __slots__ = 'name', 'geo', 'heading', 'velocity', 'radius', 'type'

    def __init__(self,
                 name: str = '',
                 lat: float = 0.0,
                 lon: float = 0.0,
                 heading: Optional[float] = None,
                 velocity: float = 0.0,
                 radius: float = 0.0,
                 type: PointType = PointType.PASS):
        self.name = name
        self.geo = GeoPoint(lat, lon)
        self.heading = heading
        self.velocity = velocity
        self.radius = radius
        self.type = type

    @property
    def lat(self):
        return self.geo.lat

    @lat.setter
    def lat(self, value):
        self.geo.lat = value

    @property
    def lon(self):
        return self.geo.lon

    @lon.setter
    def lon(self, value):
        self.geo.lon = value

    @property
    def hdg(self):
        return self.heading

    @hdg.setter
    def hdg(self, value):
        self.heading = value

    @property
    def nmeastr(self):
        return f"{abs(dd2nmea(self.geo.lat)):.4f},{self.geo.ns},{abs(dd2nmea(self.geo.lon)):010.4f},{self.geo.ew}"

    @classmethod
    def from_wp(cls, wp: WP,
                _nmea2dd = nmea2dd,
                _PASS = PointType.PASS,
                _STOP = PointType.STOP,
                _float = float):
        lat = _nmea2dd(_float(wp.lat))
        lon = _nmea2dd(_float(wp.lon))
        ptype = _PASS
        if wp.type == 'Stop':
            ptype = _STOP
        point = cls(name = wp.name,
                    lat = lat if wp.ns == 'N' else -lat,
                    lon = lon if wp.ew == 'E' else -lon,
                    heading = float(wp.heading) if wp.heading else None,
                    velocity = float(wp.velocity) if wp.velocity else 0.0, # None?
                    radius = float(wp.radius) if wp.radius else 0.0, # None?
                    type = ptype)
        return point

    @classmethod
    def from_dict(cls, js,
                  _nmea2dd = nmea2dd,
                  _float = float):
        p = js['point']
        lat, ns, lon, ew = [e.strip() for e in p.split(',')]
        lat = _nmea2dd(_float(lat))
        lon = _nmea2dd(_float(lon))
        _get = js.get
        point = cls(name = js['name'],
            lat = lat if ns == 'N' else -lat,
            lon = lon if ew == 'E' else -lon,
            heading =  _get('hdg', None),
            velocity = _get('velocity', 0.0), # None?
            radius = _get('radius', 0.0), # None?
            type = js['type'])
        return point

    def to_dict(self, only=set(), exclude=set()):
        pdict = {}
        if only:
            for key in (only  - {"geo"}):
                val = getattr(self, key)
                if val is not None:
                    if key == 'heading':
                        key = 'hdg'
                    pdict[key] = val
        else:
            for key in ('name', 'velocity', 'radius', 'type', 'heading'):
                if key not in exclude:
                    val = getattr(self, key)
                    if val is not None:
                        if key == 'heading':
                            key = 'hdg'
                        pdict[key] = val
        pdict['point'] = self.nmeastr
        return pdict

    def to_jstr(self, compact=False,
                _dumps = json.dumps):
        sep = (',', ':') if compact else None
        return _dumps(self.to_dict(), separators=sep)

    @staticmethod
    def data2geo(data: Union[GeoPoint, Tuple[float, float]]):
        return GeoPoint(data[0], data[1])


class Route:

    __slots__ = 'name', 'points', 'objectid'

    def __init__(self,
                 name: str = '',
                 points: List[RoutePoint] = [],
                 objectid: Optional[int] = None):
        self.name = name
        self.points = [p for p in points]
        self.objectid = objectid

    def __len__(self):
        return len(self.points)

    def __getitem__(self, key):
        try:
            return self.points[key]
        except TypeError:
            if isinstance(key, str):
                for p in self.points:
                    if p.name == key:
                        return p
        raise KeyError

    def __setitem__(self, key, value):
        assert isinstance(value, RoutePoint)
        try:
            self.points[key] = value
            return
        except TypeError:
            if isinstance(key, str):
                for i,p in enumerate(self.points):
                    if p.name == key:
                        self.points[i] = value
                        return
        raise KeyError

    def __iter__(self):
        yield from self.points


def route2json(route: Route, compact=False):
    jsdict = {
        'name' : route.name,
        'points': [p.to_dict() for p in route.points]
    }
    if route.objectid is not None:
        jsdict['objectid'] = route.objectid
    sep = (',', ':') if compact else None
    return json.dumps(jsdict, separators=sep)


def route_from_config(fpath):
    with open(fpath) as f:
        route = Route()
        for line in f:
            if line.startswith("Name"):
                _, name = line.split('=')
                route.name = name.strip()
            elif line.startswith("WP"):
                _, wpstr = line.split('=')
                wpvalues = wpstr.strip().split(',')
                wp = WP(*wpvalues)
                point = RoutePoint.from_wp(wp)
                route.points.append(point)
        return route
