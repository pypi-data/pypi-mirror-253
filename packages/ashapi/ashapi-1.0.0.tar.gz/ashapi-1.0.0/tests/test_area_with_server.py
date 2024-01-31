import pytest
import pytest_asyncio
import asyncio

from conftest import skip_when_no_server_running, real_server_config

from ashapi.simrequests import (
    SceneClear as RequestSceneClear,
    SceneNew as RequestSceneNew,
    SceneOpen as RequestSceneOpen,
)

from ashapi.simnettypes import AreaOrder

from ashapi.client import SimcomplexClient
from ashapi.simulation import Simulation
from ashapi.area import Area, GeoPoint
from ashapi.content import Content


pytestmark = pytest.mark.asyncio(scope="module")


@pytest_asyncio.fixture(scope='module') 
async def client():
    '''Arrange client connected to server'''
    client = SimcomplexClient(real_server_config)
    await client.connect()
    asyncio.create_task(client.run())
    yield client
    await client.disconnect()


@pytest_asyncio.fixture(scope='module') 
async def content(client):
    '''Establish content and load available areas'''
    content = Content()._attach(client)
    content.request_areas()
    await asyncio.sleep(0.1)
    yield content


async def clear_scene(client, delay=0.1):
    '''Clear scene prior running test'''
    client.send_request(RequestSceneClear())
    client.send_request(RequestSceneNew())
    client.send_message(AreaOrder())
    await asyncio.sleep(delay)


async def load_scene(client, path, delay=0.1):
    '''Load scene prior running test'''
    client.send_request(RequestSceneClear())
    client.send_request(RequestSceneOpen(path))
    await asyncio.sleep(delay)


async def do_step(client):
    sim = Simulation()._attach(client)
    sim.step()
    await asyncio.sleep(0.1)


@skip_when_no_server_running
async def test_area_clear_scene(client):

    area = Area()._attach(client)

    await clear_scene(client)

    assert area.name == ""
    assert area.origo.lat == 0.0
    assert area.origo.lon == 0.0
    assert area.meshes == []
    assert area.maps == []


@skip_when_no_server_running
async def test_area_load_empty(client):

    area = Area()._attach(client)

    await load_scene(client, 'api/empty.stexc')

    assert area.name == ""
    assert area.origo.lat == 0.0
    assert area.origo.lon == 0.0
    assert area.meshes == []
    assert area.maps == []


@skip_when_no_server_running
async def test_area_load_empty_nv(client):

    area = Area()._attach(client)

    await load_scene(client, 'api/empty_nv.stexc', delay=0.4)

    assert area.name == 'RU_NVS'
    assert area.origo.lat == 44.70139998561915
    assert area.origo.lon == 37.83500000045524
    assert area.meshes == ['RU6MELN0.json']
    assert area.maps == ['RU4MDLM0.xml', 'RU5MELN0.xml', 'RU6MELN1.xml', 'RU6MELN0.xml']


@skip_when_no_server_running
async def test_area_clear_scene_and_set_nv(content):

    client = content._client

    area = Area()._attach(client)

    await clear_scene(client)

    test_area = Area()._attach(client)

    area.set(content.areas['RU_NVS'])

    assert area.name == 'RU_NVS'
    assert area.origo.lat == 44.70139998561915
    assert area.origo.lon == 37.83500000045524
    assert area.meshes == ['RU6MELN0.json']
    assert area.maps == ['RU4MDLM0.xml', 'RU5MELN0.xml', 'RU6MELN1.xml', 'RU6MELN0.xml']

    await asyncio.sleep(0.4)

    assert test_area.name == 'RU_NVS'
    assert test_area.origo.lat == 44.70139998561915
    assert test_area.origo.lon == 37.83500000045524
    assert test_area.meshes == ['RU6MELN0.json']
    assert test_area.maps == ['RU4MDLM0.xml', 'RU5MELN0.xml', 'RU6MELN1.xml', 'RU6MELN0.xml']


@skip_when_no_server_running
async def test_area_load_empty_nv_and_then_set_opensea(client):

    area = Area()._attach(client)

    await load_scene(client, 'api/empty_nv.stexc', delay=0.2)

    test_area = Area()._attach(client)

    area.set(None) # same as area.set(OpenSea())

    assert area.name == ""
    assert area.origo.lat == 0.0
    assert area.origo.lon == 0.0
    assert area.meshes == []
    assert area.maps == []

    await asyncio.sleep(0.2)

    assert test_area.name == ""
    assert test_area.origo.lat == 0.0
    assert test_area.origo.lon == 0.0
    assert test_area.meshes == []
    assert test_area.maps == []


@skip_when_no_server_running
async def test_area_load_empty_and_set_origo(client):

    area = Area()._attach(client)

    await load_scene(client, 'api/empty.stexc')

    test_area = Area()._attach(client)

    area.origo = GeoPoint(44.70139998561915, 37.83500000045524)

    assert area.name == ""
    assert area.origo.lat == 44.70139998561915
    assert area.origo.lon == 37.83500000045524
    assert area.meshes == []
    assert area.maps == []

    await asyncio.sleep(0.1)

    assert test_area.name == ""
    assert test_area.origo.lat == 44.70139998561915
    assert test_area.origo.lon == 37.83500000045524
    assert test_area.meshes == []
    assert test_area.maps == []


