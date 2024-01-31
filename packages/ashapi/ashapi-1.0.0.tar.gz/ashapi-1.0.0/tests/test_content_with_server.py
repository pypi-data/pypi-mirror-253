import pytest
import pytest_asyncio
import asyncio

import sys

from conftest import skip_when_no_server_running, real_server_config

from ashapi.client import SimcomplexClient
from ashapi.content import Content, AreaInfo, ModelInfo

pytestmark = pytest.mark.asyncio(scope="module")


def test_modelinfo_simple():
    data = {
        'model': { 'code': 'a' },
        'contours': []
    }

    m = ModelInfo.from_dict(data)

    assert m.info == { 'code': 'a' }
    assert m.contours == []

    assert m.code == 'a'



def test_modelinfo_no_contour():

    data = {
        'model': { 'code': 'b' }
    }

    m = ModelInfo.from_dict(data)

    assert m.info == { 'code': 'b' }
    assert m.contours == []

    assert m.code == 'b'


def test_modelinfo_contours_split():

    data = {
        'model': { 'code': 'c' },
        'contours': [
            [1, 2, 3, 4],
            [-1, -2, -3, -4, -5, -6],
        ]
    }

    m = ModelInfo.from_dict(data)

    assert m.contours == [
        [(1,2), (3,4)],
        [(-1, -2), (-3, -4), (-5, -6)]
    ]


@pytest_asyncio.fixture(scope='module')
async def client():
    '''Arrange client connected to server'''
    client = SimcomplexClient(real_server_config)
    await client.connect()
    asyncio.create_task(client.run())
    yield client
    await client.disconnect()


@skip_when_no_server_running
async def test_content_after_connected(client):

    content = Content()._attach(client)

    await asyncio.sleep(0.1)

    assert len(content.scenes) == 0
    assert len(content.recordings) == 0
    assert len(content.models) == 0
    assert len(content.areas) == 0

    content._detach()


@skip_when_no_server_running
async def test_content_scenes(client):

    content = Content()._attach(client)

    content.request_scenes()

    await asyncio.sleep(0.1)

    assert len(content.scenes) > 30 #TODO: process

    assert 'api/empty.stexc' in content.scenes
    assert 'api/empty_nv.stexc' in content.scenes
    assert 'api/routes/route_01.stexc' in content.scenes

    assert len(content.recordings) == 0
    assert len(content.models) == 0
    assert len(content.areas) == 0

    content._detach()


@skip_when_no_server_running
async def test_content_recordings(client):

    content = Content()._attach(client)

    content.request_recordings()

    await asyncio.sleep(0.1)

    assert len(content.recordings) >= 2

    assert f"запись.strec" in content.recordings
    assert f"api/recordings/misv01_accelerating_01.strec" in content.recordings

    assert len(content.scenes) == 0
    assert len(content.models) == 0
    assert len(content.areas) == 0

    content._detach()


@skip_when_no_server_running
async def test_content_models(client):

    content = Content()._attach(client)

    content.request_models()

    await asyncio.sleep(0.1)

    assert len(content.models) == 28 #TODO: process

    assert len(content.scenes) == 0
    assert len(content.recordings) == 0
    assert len(content.areas) == 0

    content._detach()


@skip_when_no_server_running
async def test_content_model_image(client):

    content = Content()._attach(client)

    image = None
    def on_image(response):
        nonlocal image
        image = response

    content.request_model_image('misv01', on_image)

    await asyncio.sleep(0.1)

    assert image is not None
    assert sys.getsizeof(image) >= 270085

    content._detach()


@skip_when_no_server_running
async def test_content_model_image1(client):

    content = Content()._attach(client)

    image = None
    def on_image(response):
        nonlocal image
        image = response

    content.request_models()
    content.request_model_image('misv01', on_image)

    await asyncio.sleep(0.2)

    assert image is not None
    assert sys.getsizeof(image) >= 270085

    assert content.models['misv01'].image == image

    content._detach()


@skip_when_no_server_running
async def test_content_areas(client):

    content = Content()._attach(client)

    content.request_areas()

    await asyncio.sleep(0.1)

    assert len(content.models) == 0 
    assert len(content.scenes) == 0
    assert len(content.recordings) == 0

    assert len(content.areas) == 5

    assert 'RU_NVS' in content.areas

    nv = content.areas['RU_NVS']

    assert isinstance(nv, AreaInfo)

    content._detach()


@skip_when_no_server_running
async def test_content_area_image(client):

    content = Content()._attach(client)

    image = None
    def on_image(response):
        nonlocal image
        image = response

    content.request_area_image('RU_NVS', on_image)

    await asyncio.sleep(0.1)

    assert len(content.areas) == 0

    assert image is not None
    assert sys.getsizeof(image) >= 689534

    content._detach()


@skip_when_no_server_running
async def test_content_area_image1(client):

    content = Content()._attach(client)

    image = None
    def on_image(response):
        nonlocal image
        image = response

    content.request_areas()
    content.request_area_image('RU_NVS', on_image)

    await asyncio.sleep(0.1)

    assert image is not None
    assert sys.getsizeof(image) >= 689534

    assert content.areas['RU_NVS'].image == image

    content._detach()


@skip_when_no_server_running
async def test_content_area_map(client):

    content = Content()._attach(client)

    amap = None
    def on_map(response):
        nonlocal amap
        amap = response

    content.request_area_map('RU_NVS', 'RU6MELN0.xml', on_map)

    await asyncio.sleep(0.1)

    assert len(content.areas) == 0

    assert amap is not None
    assert sys.getsizeof(amap) >= 1219937

    content._detach()


@skip_when_no_server_running
async def test_content_area_map1(client):

    content = Content()._attach(client)

    amap = None
    def on_map(response):
        nonlocal amap
        amap = response

    content.request_areas()
    content.request_area_map('RU_NVS', 'RU6MELN0.xml', on_map)

    await asyncio.sleep(0.1)

    assert amap is not None
    assert sys.getsizeof(amap) >= 1219937

    assert content.areas['RU_NVS'].mapsdata['RU6MELN0.xml'] == amap

    content._detach()
