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

import aiohttp
import asyncio
import subprocess
import time

from multiprocessing import Process
from contextlib import contextmanager

from typing import Callable

import logging


from . config import Config
from . simulation import Simulation
from . scene import Scene
from . environment import Environment
from . content import Content
from . client import SimcomplexClient

from . events import Events

from . simrequests import SimulationState as RequestSimulationState


logger = logging.getLogger("Simcomplex")
formatter = logging.Formatter(fmt="%(levelname)s | %(name)s | %(asctime)s | %(message)s")
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)


async def check_server_ready(url, timeout=1.0):
    try:
        timeout = aiohttp.ClientTimeout(connect=timeout)
        async with aiohttp.ClientSession(url, timeout=timeout) as session:
           resource = RequestSimulationState.resource
           async with session.get(resource) as resp:
              if resp.status == 200:
                 return True
    except aiohttp.ClientConnectionError:
        return False


def is_server_running(url, timeout=1.0):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return loop.run_until_complete(check_server_ready(url, timeout))


def run_local_server_subprocess(server_folder, debug=False):
    if debug:
        start = f'npm run start{":debug" if debug else ""}'
    else:
        start = f'node server.js'
    try:
        proc = subprocess.Popen(start, 
                                cwd = server_folder,
                                shell = True,
                                stdout=subprocess.DEVNULL,
                                stderr=subprocess.DEVNULL)
        return proc.wait()
    except:
        return 1


@contextmanager
def local_server(config, debug=False):
    logger = logging.getLogger("Simcomplex")
    server_process = None
    running = is_server_running(config.http_uri)
    if not running:
        logger.info(f'Simulation server is not running, attempt to start local server...')
        local_server_path = config.local_server_path
        if not local_server_path:
            raise RuntimeError(f"Path to simcomlex is invalid: '{local_server_path}'")
        server_process = Process(
            target = run_local_server_subprocess,
            args=(local_server_path, debug)
        )
        server_process.start()
        timeout = 5.0
        dt = 0.1
        while timeout > 0 and server_process.is_alive() and not running:
            time.sleep(dt)
            timeout -= dt
            running = is_server_running(config.http_uri)
        if running and server_process.is_alive():
            logger.info(f"Started local simulation server in {5.0 - timeout:.3f} seconds")
        else:
            raise RuntimeError("Failed to start local simulation server")
    yield server_process
    if server_process:
        logger.info(f"Stopping local simulation server")
        server_process.terminate()



class Simcomplex:

    def __init__(self, config: Config):
        self._client =  SimcomplexClient(config)
        self._simulation = Simulation()._attach(self._client)
        self._scene = Scene()._attach(self._client)
        self._environment = Environment()._attach(self._client)
        self._content = Content()._attach(self._client)
        self._logger = logging.getLogger("Simcomplex")

    @property
    def config(self):
        return self._client.config

    @property
    def simulation(self):
        return self._simulation

    @property
    def scene(self):
        return self._scene

    @property
    def environment(self):
        return self._environment

    @property
    def content(self):
        return self._content

    def shutdown(self):
        self._content._detach()
        self._environment._detach()
        self._scene._detach()
        self._simulation._detach()


class SimcomplexTask(Simcomplex):

    def __init__(self, config: Config, *args, **kwargs):
        super().__init__(config)
        self.init(*args, **kwargs)

    def init(self, *args, **kwargs):
        '''
        Called once when task is being constructed.
        Can be overridden by inherited classes - user specific tasks.
        Can be used to initialize additional variables, do some pre-calculations etc.
        prior task starts connecting to simcomplex scene.
        '''
        pass

    def connected(self):
        '''
        Called once when task connected to simcomplex.
        At this moment task is already connected, so can send requests to server.
        Keep in mind that simulation state is not fully determined at this stage,
        because task may be still receiving simulation scene state updates at this moment.
        Can be overridden by inherited classes - user specific tasks.
        Can be used to query for content or to do some very specific actions.
        '''
        pass

    def setup(self):
        '''
        Called once when task connected to simcomplex and got first CONTENT_CREATED event.
        At this moment task is fully aware of all the state of the simulation scene.
        Can be overridden by inherited classes - user specific tasks.
        Can be used to set-up simulation for user needs - e.g. create new scene, stop/run simulation, query for content etc.
        '''
        pass

    def on_event(self,
                 event: Events,
                 action: Callable = lambda payload: None,
                 persist: Callable = lambda: False):
        '''
        Subscribe task to run given action on particular event.
        If 'persist' function is provided, task performs action each time event is triggered, until persist() returns False.
        Once persist() return False, task unsubscribes from event.
        '''
        def do_action(payload):
            action(payload)
            if not persist():
                self._client.unsubscribe(event, do_action)
        self._client.subscribe(event, do_action)


    def run(self):
        # asyncio.run(self.__run(), debug=True)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        return loop.run_until_complete(self.__run())

    def complete(self):
        super().shutdown()
        self._client.shutdown()

    def result(self):
        return True

    async def __run(self):
        self._client.subscribe(Events.CONNECTED, self._first_connected)
        self._client.subscribe(Events.CONTENT_CREATED, self._first_content_created)
        await self._client.connect()
        client_run_task = asyncio.create_task(self._client.run())
        await client_run_task
        await self._client.disconnect()
        return self.result()

    def _first_connected(self, payload=None):
        self.connected()
        self._client.unsubscribe(Events.CONNECTED, self._first_connected)

    def _first_content_created(self, payload=None):
        self.setup()
        self._client.unsubscribe(Events.CONTENT_CREATED, self._first_content_created)



if __name__ == "__main__":

    from pprint import pprint

    class MyTask(SimcomplexTask):

        def init(self):
            self.image = None
            self.content.request_areas(self.on_areas)

        def on_areas(self, _):
            pprint(self.content.areas)
            if 'RU_NVS' in self.content.areas:
                return self.content.request_area_image('RU_NVS', self.on_image)
            raise RuntimeError

        def on_image(self, _):
            self.image = self.content.areas['RU_NVS'].image
            self.complete()

        def result(self):
            print(f"RU_NVS image is: {self.image}")
            return self.image


    logging.basicConfig(level=logging.INFO)

    logger = logging.getLogger("Simcomplex")
    logger.propagate = False

    config = Config.localhost(simcomplex='C:\git\simcomplex')

    task = MyTask(config)


    with local_server(config, debug=True):
        result = task.run()
        print(f"Task done with result: {result}")

