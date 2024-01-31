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

from typing import Optional, Union, List

from math import degrees, radians


from . simnettypes import (
    Area as AreaNetType,
    AreaOrder,
    AreaOrigin,
    AreaOriginOrder,
)

from . events import Events
from . proxy import SimDataClient

from . geo import GeoPoint, Euler, lla2ecef, get_ltp_quat
from . pq import PQ


class AreaInfo:

    __slots__ = "info", "image", "mapsdata"

    def __init__(self, info: dict):
        self.info = info
        self.image = None # keeps downloaded image
        self.mapsdata = {} # keeps downloaded mapsdata

    @property
    def name(self):
        return self.info.get('name', '')

    @property
    def title(self):
        return self.info.get('title', '')

    @property
    def description(self):
        return self.info.get('description', '')

    @property
    def origo(self):
        return self.info.get('origo', None)

    @property
    def meshes(self):
        return self.info.get('meshes', [])

    @property
    def maps(self):
        return self.info.get('maps', [])

    def __str__(self):
        return f"AreaInfo '{self.name}' '{self.title}', origo={self.origo}"

    def __repr__(self):
        return f'AreaInfo({self.info})'


class OpenSeaInfo(AreaInfo):

    __slots__ = []

    def __init__(self, origo = [0.0, 0.0]):
        super().__init__({
            'name': "",
            'title': "Открытое море",
            'description': ["Открытое море"],
            'origo': origo,
            'meshes': [],
            'maps': []
        })


class Area(SimDataClient):

    __slots__ = "_data",

    def __init__(self):
        self._data = { 'name': "", 'origo': [0.0, 0.0], 'meshes': [], 'maps': [] }

    def _subscribe(self):
        self._client.subscribe(Events.AREA, self.on_area)
        self._client.subscribe(Events.AREA_ORIGIN, self.on_area_origin)
        return self

    def _unsubscribe(self):
        if self._client:
            self._client.unsubscribe(Events.AREA_ORIGIN, self.on_area_origin)
            self._client.unsubscribe(Events.AREA, self.on_area)
        return self

    def set(self,
            area: Optional[AreaInfo] = None,
            origo: Optional[Union[GeoPoint, List]] = None):
        if area is None: # open sea
            area = OpenSeaInfo([0.0, 0.0] if origo is None else self._make_origo(origo))
        self.from_info(area)
        self._send(AreaOrder(**self._data))

    @property
    def name(self) -> str:
        return self._data['name']

    @property
    def origo(self) -> GeoPoint:
        return GeoPoint(degrees(self._data['origo'][0]), degrees(self._data['origo'][1]))

    @origo.setter
    def origo(self, value: Union[GeoPoint, List]) -> None:
        self._data['origo'] = self._make_origo(value)
        self._send(AreaOriginOrder(*self._data['origo']))

    @property
    def meshes(self) -> list:
        return self._data['meshes']

    @property
    def maps(self) -> list:
        return self._data['maps']

    @property
    def ecef(self) -> PQ:
        ''' Returns ECEF position and orientation of area origo '''
        return PQ(lla2ecef(self.origo), get_ltp_quat(self.origo))

    #
    # Simulation server events handlers
    #

    def on_area(self, state: AreaNetType):
        self._data = state.data

    def on_area_origin(self, state: AreaOrigin):
        self._data['origo'] = [state.lat, state.lon] # radians


    @staticmethod
    def _make_origo(o: Union[GeoPoint, List],
                   _rad = radians):
        return [_rad(o[0]), _rad(o[1])]


    def from_info(self, info: AreaInfo):
        self._data = {
            'name': info.info['name'],
            'origo': info.info['origo'][:],
            'meshes': info.info['meshes'][:],
            'maps': info.info['maps'][:]
        }

    def __str__(self):
        return f"Area '{self.name}', origo={self.origo}, maps={self.maps}"

    def __repr__(self):
        return f'Area() # name={self.name}, origo={self._data["origo"]}, maps={self.maps}'
