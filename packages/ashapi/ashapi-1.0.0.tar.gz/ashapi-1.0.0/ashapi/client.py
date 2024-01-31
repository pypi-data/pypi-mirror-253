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

import logging
from aiohttp import ClientSession, ClientTimeout, WSMsgType

import asyncio

from collections import deque
from contextlib import asynccontextmanager
from datetime import datetime
from time import time
from typing import Callable, Optional, Deque

from . config import Config
from . events import Events, EventBus
from . timer import Timer, call_at, wait_until
from . simnettypes import nettypes_factory, NetType
from . simrequests import SimRequest


logger = logging.getLogger("ashapi.client")
formatter = logging.Formatter(fmt="%(levelname)s | %(name)s | %(message)s")
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)


class ClientConnectedTimer(Timer):

    __slots__ = ["client"]

    def __init__(self, client):
        super().__init__()
        self.client = client

    def span(self):
        if self.client.connected:
            return super().span()
        return self.t1 - self.t0


class SimcomplexClient:

    def __init__(self,
                 config: Config = Config.localhost()):
        self.config = config
        self.eventbus = EventBus()
        self.session = None # will be aihttp.ClientSession when connect() called
        self.requests_send_queue: Deque = deque()
        self.process_requests: asyncio.Task = None
        self.websocket = None # will be aihttp.ClientWebSocketResponse when connect() called
        self.websocket_send_queue: Deque = deque()
        self.process_websocket: asyncio.Task = None
        self.connected: bool = False
        self.shutdown_requested = asyncio.Event()
        self.timer = ClientConnectedTimer(self) # measures for how long client is connected
        self.subscribe(Events.CONNECTED, self.__on_connect)
        self.subscribe(Events.DISCONNECTED, self.__on_disconnect)
        self.subscribe(Events.CONNECTION_REFUSED, self.__on_disconnect)
        self.logger = logging.getLogger("ashapi.client")


    def send_message(self, nettype: NetType):
        self.websocket_send_queue.append(nettype.to_jstr())

    def send_request(self,
                     simrequest: SimRequest,
                     response_handler: Callable[[str], None] = lambda s: None):
        self.requests_send_queue.append((simrequest, response_handler))

    def subscribe(self, event_type, event_handler):
        self.eventbus.add_listener(event_type, event_handler)

    def unsubscribe(self, event_type, event_handler):
        self.eventbus.remove_listener(event_type, event_handler)


    async def connect(self):
        self.logger.debug("Simcomplex connect requested")
        timeout = ClientTimeout(connect=1.0)
        self.session = ClientSession(base_url=self.config.http_uri, timeout=timeout)
        try:
            self.websocket = await self.session.ws_connect(self.config.ws_resource)._coro
        except asyncio.TimeoutError as e:
            self.logger.error("Simcomplex websocket connection refused")
            self.eventbus.emit(Events.CONNECTION_REFUSED)
        else:
            self.eventbus.emit(Events.CONNECTED)


    async def disconnect(self):
        self.logger.debug("SimcomplexClient requested disconnect")
        self.shutdown()
        if self.websocket:
            await self.websocket.close()
        await self.session.close()
        self.connected = False


    def __on_connect(self, data=None):
        self.logger.debug("SimcomplexClient connected")
        self.connected = True
        self.timer.reset()


    def __on_disconnect(self, data=None):
        self.logger.debug("SimcomplexClient disconnected")
        self.connected = False
        if self.config.autoreconnect:
            self.logger.info("Attempt to reconnect...")
            asyncio.get_running_loop().create_task(self.connect())


    def __handle_websocket_message(self, timestamp, msg, 
                                   _msg_reader=nettypes_factory):
        self.logger.debug(f'{datetime.fromtimestamp(timestamp)}: {msg}')
        nettype = _msg_reader(msg)
        if nettype:
            self.eventbus.emit(nettype.type, nettype)


    def shutdown(self, _task=None):
        if self.process_websocket:
            self.process_websocket.cancel()
            self.logger.debug("SimcomplexClient: shut down websocket processing")
        if self.process_requests:
            self.process_requests.cancel()
            self.logger.debug("SimcomplexClient: shut down requests processing")


    async def run(self,
                  duration: Optional[float] = None):

        timer_task = None

        if duration is not None:
            timer_task = asyncio.create_task(wait_until(duration, Timer().span))
            timer_task.add_done_callback(self.shutdown)

        _sleep = asyncio.sleep

        while not self.connected:
            await _sleep(0.1)
            if timer_task and timer_task.done():
                break

        while self.connected:

            self.process_requests = asyncio.create_task(self.__process_requests())
            self.process_websocket = asyncio.create_task(self.__process_websocket())

            try:
                await self.process_websocket
                await self.process_requests
            except ConnectionError as e:
                self.eventbus.emit(Events.DISCONNECTED)
            except asyncio.CancelledError:
                pass
            except RuntimeError:
                pass

            try:
                await self.websocket.close()
            except Exception as e:
                self.logger.debug(f"SimcomplexClient: problem closing websocket: {e}")

            try:
                await self.session.close()
            except Exception as e:
                self.logger.debug(f"SimcomplexClient: problem closing session: {e}")

            self.connected = False

        self.logger.debug("SimcomplexClient: finished running")


    async def __process_requests(self):
        _requests = self.requests_send_queue
        _pop = _requests.popleft
        _send = self.session.request
        _sleep = asyncio.sleep
        while True:
            try:
                while _requests:
                    simrequest, handler =_pop()
                    async with _send(simrequest.method, 
                                    simrequest.resource, 
                                    params = simrequest.params) as response:
                        if response.content_type.startswith("image"):
                            blob = await response.read()
                            handler(blob)
                        else:
                            text = await response.text()
                            handler(text)
            except asyncio.CancelledError:
                self.logger.debug("SimcomplexClient: shut down requests processing")
                return
            except Exception as e:
                self.logger.exception(e)
                self.shutdown()
                return
            await _sleep(0)


    async def __process_websocket(self):

        async def send(fsend, q):
            _pop = q.popleft
            _sleep = asyncio.sleep
            while True:
                while q:
                    await fsend(_pop())
                await _sleep(0)

        async def recv(frecv, handler):
            TEXT = WSMsgType.TEXT
            CLOSED = WSMsgType.CLOSED
            _time = time
            while True:
                msg = await frecv()
                if msg.type == TEXT:
                    timestamp = _time()
                    handler(timestamp, msg.data)
                elif msg.type == CLOSED:
                    break

        send_task = asyncio.create_task(send(self.websocket.send_str, self.websocket_send_queue))
        recv_task = asyncio.create_task(recv(self.websocket.receive, self.__handle_websocket_message))

        # websocket read/write main cycle

        while True:
            try:
                await send_task
                await recv_task
            except asyncio.CancelledError:
                break

        # clean-up and finish

        self.logger.debug("SimcomplexClient: shutting down websocket read/write")
        send_task.cancel()
        try:
            await send_task
        except asyncio.CancelledError: 
            self.logger.debug("SimcomplexClient: shut down websocket write (send)")
        recv_task.cancel()
        try:
            await recv_task
        except asyncio.CancelledError: 
            self.logger.debug("SimcomplexClient: shut down websocket read (recv)")


    def call_at(self, t: Optional[float] = None) -> Callable:
        ''' Schedule a call after t seconds of client connected time '''
        return call_at(t, self.timer)


@asynccontextmanager
async def connected(config: Config):
    client = SimcomplexClient(config)
    await client.connect()
    client_run_task = asyncio.create_task(client.run())
    yield client
    await client_run_task
    await client.disconnect()

#
# Debug
#

def print_timestamp_and_message(t, msg_str,
                                _print = print,
                                _frmt = datetime.fromtimestamp):
    _print(f'{_frmt(t)}: {msg_str}')


def print_response_text(response,
                        _print = print,
                        _time = time,
                        _frmt = datetime.fromtimestamp):
    timestamp = _time()
    _print(f'{_frmt(timestamp)}: {response.text}')


def print_text(text,
               _print = print,
               _time = time,
               _frmt = datetime.fromtimestamp):
    timestamp = _time()
    _print(f'{_frmt(timestamp)}: {text}')
