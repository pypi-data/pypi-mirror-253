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

from . simnettypes import NetType
from . simrequests import SimRequest

from . client import SimcomplexClient


class SimDataClient:

    __slots__ = "_client",

    @property
    def client(self):
        return self._client

    def _attach(self, client: SimcomplexClient):
        self._client = client
        self._subscribe()
        return self

    def _detach(self):
        if self._client:
            self._unsubscribe()
            self._client = None
        return self

    def _subscribe(self):
        ''' To be overridden by inherited classes, called when attaching to simcomplex client '''
        pass

    def _unsubscribe(self):
        ''' To be overridden by inherited classes, called when detaching from simcomplex client '''
        pass

    def _send(self, message: NetType):
        if self._client:
            self._client.send_message(message)

    def _receive(self, message: NetType):
        self._data.update(message.data)

    def _request(self, 
                 request: SimRequest,
                 on_response: Callable[[str], None] = lambda response_text: None):
        if self._client:
            self._client.send_request(request, on_response)


    def _all_slots(self, _type=type):
        for cls in _type(self).__mro__:
            yield from cls.__dict__.get('__slots__', ())


    def __getattr__(self, name):
        if name in set(self._all_slots()):
            return object.__getattribute__(self, name)
        return self._getattr(name)


    def _getattr(self, name, _get=getattr):
        ''' To be overridden by inherited classes, called when no attibute found in __slots__'''
        return _get(self, name)


    def __setattr__(self, name, value):
        try:
            object.__setattr__(self, name, value)
        except AttributeError:
            self._setattr(name, value)


    def _setattr(self, name, value):
        ''' To be overridden by inherited classes, called when assigning to attribute which is not in __slots__'''
        pass
