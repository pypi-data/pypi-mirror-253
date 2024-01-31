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

from typing import Optional, Callable, Dict

from pathlib import PurePath
from itertools import groupby

import json

from . proxy import SimDataClient

from . area import AreaInfo

from . simrequests import (
    Exercises as RequestExercises,
    Recordings as RequestRecordings,
    Models as RequestModels,
    ModelImage as RequestModelImage,
    Areas as RequestAreas,
    AreaImage as RequestAreaImage,
    AreaMap as RequestAreaMap
)



def iter_files(structure, root='', filter=".stexc", _path=PurePath):
    for entry in structure:
        if 'directory' in entry and 'content' in entry:
            directory = _path(entry['directory'])
            yield from iter_files(entry['content'], _path(root, directory), filter) #  if root else directory)
        elif 'name' in entry and 'modified' in entry:
            name = entry['name']
            if not filter or name.endswith(filter):
                yield _path(root, name), entry['modified']


class FilesStructure:

    def __init__(self):
        self._files = {}

    @classmethod
    def from_dict(cls, d, filter=".stexc"):
        files = cls()
        files._files = { file : modified for file, modified in iter_files(d, '', filter)}
        return files

    def __len__(self):
        return len(self._files)

    def __contains__(self, path):
        return PurePath(path) in self._files

    def __iter__(self):
        yield from self._files


class DeviceInfo:

    __slots__ = "_data"

    def __init__(self, data):
        self._data = data

    @property
    def tag(self):
        return self._data['tag']

    @property
    def group(self):
        return self._data.get('group', '')

    @property
    def type(self):
        return self._data.get('physics', '')[8:]

    @property
    def params(self):
        return {key: value for key, value in self._data.items() if key not in {'tag', 'group', 'physics', 'chart'}}

    @property
    def position(self):
        return self._data.get('translate')

    def __getattr__(self, name):
        data = object.__getattribute__(self, "_data")
        if name == "_data":
            return data
        value = data.get(name, {})
        if not isinstance(value, dict):
            return value


class DevicesInfo:

    __slots__ = "_devices",

    def __init__(self):
        self._devices = {}

    @classmethod
    def from_dict(cls, subobjects,
                  _device = DeviceInfo):
        devices = cls()
        devices._devices = { s['tag']: _device(s) for s in subobjects }
        return devices

    def __len__(self):
        return len(self._devices)

    def __getitem__(self, index):
        if isinstance(index, str):
            return self._devices.get(index, None)
        return list(self)[index]

    def get_grouped(self,
                    type: str = '',
                    group: str = ''):
        grouped = [d for d in self if d.group == group] if group else list(self)
        if type:
            typo = type[8:] if type.startswith("physics.") else type
            grouped = [d for d in grouped if d.type == typo]
        return grouped

    def iter_grouped(self):
        yield from groupby(sorted(self, key = lambda d: d.type), key = lambda d: d.type)

    def __contains__(self, tag):
        return tag in self._devices

    def __iter__(self):
        yield from self._devices.values()


class ModelInfo:

    __slots__ = "info", "devices", "contours", "image"

    def __init__(self):
        self.info = {}
        self.contours = []
        self.devices = DevicesInfo()
        self.image = None

    @classmethod
    def from_dict(cls, d,
                  _tuple = tuple,
                  _range = range,
                  _len = len):
        model = cls()
        model.info = { key: value for key, value in d.get('model', {}).items() if key != 'subobjects' }
        model.devices = DevicesInfo.from_dict(d.get('model', {}).get('subobjects', {}))
        model.contours = [[_tuple(c[i:i+2]) for i in _range(0, _len(c), 2)] for c in d.get('contours', [])]
        return model

    def __getattr__(self, name):
        if name in ("info", "devices", "contours", "image"):
            return object.__getattribute__(self, name)
        info = object.__getattribute__(self, "info")
        return info[name] if name in info else None

    # def __setattr__(self, name, value):
    #     if name in ("info", "contours", "image"):
    #         object.__setattr__(self, name, value)

    @property
    def length(self):
        return (self.info.get("hydromodel2d", {}) or self.info.get("aeromodel2d", {})).get("length", None)

    @property
    def beam(self):
        return self.info.get("hydromodel2d", {}).get("beam", None)

    @property
    def height(self):
        return self.info.get("aeromodel2d", {}).get("height", None)

    @property
    def draught(self):
        return self.info.get("hydromodel2d", {}).get("draught", 0) or -self.info.get("draft", 0)

    @property
    def cms(self):
        ''' Returns model center of mass '''
        return self.info.get("translate", [0, 0, 0])


class Content(SimDataClient):

    __slots__ = "_models", "_areas", "_scenes", "_recordings"

    def __init__(self):
        self._models: Dict[str, ModelInfo]= {}
        self._areas: Dict[str, AreaInfo] = {}
        self._scenes: FilesStructure = FilesStructure()
        self._recordings: FilesStructure = FilesStructure()

    #
    # Scenes
    #

    @property
    def scenes(self):
        return self._scenes

    def request_scenes(self, on_response: Optional[Callable[[str], None]] = None):
        def on_scenes(response):
            js = json.loads(response)
            self._scenes = FilesStructure.from_dict(js, filter = ".stexc")
            if on_response is not None:
                on_response(response)
        self._request(RequestExercises(), on_scenes)

    #
    # Recordings
    #

    @property
    def recordings(self):
        return self._recordings

    def request_recordings(self, on_response: Optional[Callable[[str], None]] = None):
        def on_recordings(response):
            js = json.loads(response)
            self._recordings = FilesStructure.from_dict(js, filter = ".strec")
            if on_response is not None:
                on_response(response)
        self._request(RequestRecordings(), on_recordings)

    #
    # Models
    #

    @property
    def models(self):
        return self._models

    def request_models(self, on_response: Optional[Callable[[str], None]] = None):
        def on_models(response):
            js = json.loads(response)
            self._models = { code : ModelInfo.from_dict(entry) for code, entry in js.items() }
            if on_response is not None:
                on_response(response)
        self._request(RequestModels(), on_models)

    def on_got_models(self, response_text: str):
        self._models = json.loads(response_text)


    def request_model_image(self,
                            code: str,
                            on_response: Callable[[str], None] = lambda response_text: None):
        def on_image(response):
            if code in self._models:
                self._models[code].image = response
            if on_response is not None:
                on_response(response)
        self._request(RequestModelImage(code), on_image)


    #
    # Areas
    #

    @property
    def areas(self):
        return self._areas

    def request_areas(self, on_response: Optional[Callable[[str], None]] = None):
        def on_areas(response):
            js = json.loads(response)
            self._areas = { key: AreaInfo(value) for key,value in js.items() }
            if on_response is not None:
                on_response(response)
        self._request(RequestAreas(), on_areas)

    def request_area_image(self,
                           code: str,
                           on_response: Callable[[str], None] = lambda response: None):
        def on_image(response):
            if code in self._areas:
                self._areas[code].image = response
            if on_response is not None:
                on_response(response)
        self._request(RequestAreaImage(code), on_image)

    def request_area_map(self,
                         code: str,
                         mapname: str,
                         on_response: Callable[[str], None] = lambda response_text: None):
        def on_amap(response):
            if code in self._areas:
                self._areas[code].mapsdata[mapname] = response
            if on_response is not None:
                on_response(response)
        self._request(RequestAreaMap(code, mapname), on_amap)


