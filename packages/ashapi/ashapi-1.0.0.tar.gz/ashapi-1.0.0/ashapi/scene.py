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

from typing import Callable

from . simrequests import SceneClear, SceneNew, SceneOpen, SceneSave, RecordingOpen, RecordingSave
from . simnettypes import ContentDeleted, ContentCreated

from . events import Events
from . proxy import SimDataClient

from . area import Area
from . objects import Objects
from . routes import Routes


class Scene(SimDataClient):

    __slots__ = "_path", "_area", "_objects", "_routes"

    def __init__(self):
        self._path = ''
        self._area = Area()
        self._objects = Objects(self._area)
        self._routes = Routes()

    def _subscribe(self):
        self._client.subscribe(Events.CONTENT_DELETED, self.on_content_deleted)
        self._client.subscribe(Events.CONTENT_CREATED, self.on_content_created)
        self._area._attach(self._client)
        self._objects._attach(self._client)
        self._routes._attach(self._client)
        return self

    def _unsubscribe(self):
        if self._client:
            self._routes._detach()
            self._objects._detach()
            self._area._detach()
            self._client.unsubscribe(Events.CONTENT_CREATED, self.on_content_created)
            self._client.unsubscribe(Events.CONTENT_DELETED, self.on_content_deleted)
        return self


    @property
    def path(self):
        return self._path

    @property
    def area(self):
        return self._area

    @property
    def objects(self):
        return self._objects


    @property
    def routes(self):
        return self._routes

    #
    # Requests to simulation server
    #

    def clear(self, 
              on_response: Callable[[str], None] = lambda response_text: None):
        self._request(SceneClear(), on_response)

    def new(self,
            on_response: Callable[[str], None] = lambda response_text: None):
        self._request(SceneNew(), on_response)

    def new_path(self,
            path: str,
            on_response: Callable[[str], None] = lambda response_text: None):
        self._request(SceneNew(path), on_response)

    def open(self,
             path: str,
             on_response: Callable[[str], None] = lambda response_text: None):
        if path.endswith('.stexc'):
            self._request(SceneOpen(path), on_response)
        if path.endswith('.strec'):
            self._request(RecordingOpen(path), on_response)

    def save(self,
             path: str,
             on_response: Callable[[str], None] = lambda response_text: None):
        self._request(SceneSave(path), on_response)

    def save_recording(self,
                       path: str,
                       on_response: Callable[[str], None] = lambda response_text: None):
        self._request(RecordingSave(path), on_response)


    #
    # Simulation server events handlers
    #

    def on_content_deleted(self, state: ContentDeleted):
        self._path = ''
        self._objects.clear()
        self._routes.clear()


    def on_content_created(self, state: ContentCreated):
        self._path = state.path
