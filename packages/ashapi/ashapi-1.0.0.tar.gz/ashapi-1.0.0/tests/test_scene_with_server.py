import pytest
import pytest_asyncio
import asyncio
import json

from conftest import skip_when_no_server_running, real_server_config

from ashapi.simrequests import (
    SceneClear as RequestSceneClear,
    SceneNew as RequestSceneNew,
    SceneOpen as RequestSceneOpen,
    SimulationState as RequestSimulationState
)

from ashapi.client import SimcomplexClient
from ashapi.scene import Scene

from ashapi.route import Route, RoutePoint, PointType

from ashapi import GeoPoint, Euler, Vec3, Quat


#
# https://stackoverflow.com/questions/56236637/using-pytest-fixturescope-module-with-pytest-mark-asyncio
#
# https://pytest-asyncio.readthedocs.io/en/latest/how-to-guides/run_module_tests_in_same_loop.html
#

# @pytest.fixture(scope="module")
# def event_loop():
#     loop = asyncio.get_event_loop_policy().new_event_loop()
#     yield loop
#     loop.close()

pytestmark = pytest.mark.asyncio(scope="module")


@pytest_asyncio.fixture(scope='module') 
async def client():
    '''Arrange client connected to server'''
    client = SimcomplexClient(real_server_config)
    await client.connect()
    asyncio.create_task(client.run())
    yield client
    await client.disconnect()


async def clear_scene(client):
    '''Clear scene prior running test'''
    client.send_request(RequestSceneClear())
    client.send_request(RequestSceneNew())
    await asyncio.sleep(0.1)


async def load_scene(client, path, delay=0.1):
    '''Load scene prior running test'''
    client.send_request(RequestSceneClear())
    client.send_request(RequestSceneOpen(path))
    await asyncio.sleep(delay)


@skip_when_no_server_running
async def test_scene_clear(client):

    scene = Scene()
    scene._attach(client)
    scene._path = 'some'

    clear_scene_response = ""
    def on_scene_cleared(response_text):
        nonlocal clear_scene_response
        js = json.loads(response_text)
        clear_scene_response = js['message']

    scene.clear(on_scene_cleared)

    await asyncio.sleep(0.5)

    assert clear_scene_response == "scene is cleared"
    assert scene.path == ''
    assert len(scene._objects) == 0
    assert len(scene._routes) == 0

    scene._detach()


@skip_when_no_server_running
async def test_scene_new(client):

    scene = Scene()
    scene._attach(client)

    new_scene_response = ""
    def on_scene_new(response_text):
        nonlocal new_scene_response
        js = json.loads(response_text)
        new_scene_response = js['message']

    scene.new(on_scene_new)

    await asyncio.sleep(0.5)

    assert new_scene_response == "empty scene is created with path "

    scene._detach()


@skip_when_no_server_running
async def test_scene_new_path(client):

    scene = Scene()
    scene._attach(client)

    responses = []
    def on_scene_new(response_text):
        js = json.loads(response_text)
        responses.append(js['message'])

    scene.new_path(r"api\new_scene", on_scene_new)

    await asyncio.sleep(0.5)

    assert responses == [r"empty scene is created with path api\new_scene"]

    scene._detach()


@skip_when_no_server_running
async def test_scene_open_empty(client):

    await clear_scene(client)

    scene = Scene()
    scene._attach(client)

    open_scene_response = ""
    def on_scene_opened(response_text):
        nonlocal open_scene_response
        js = json.loads(response_text)
        open_scene_response = js['message']

    scene.open('api/empty.stexc', on_scene_opened)

    await asyncio.sleep(0.5)

    assert open_scene_response == "scene is opened"
    assert scene.path == 'api/empty.stexc'

    scene._detach()


@skip_when_no_server_running
async def test_scene_open_api_routes_route_01(client):

    await clear_scene(client)

    scene = Scene()
    scene._attach(client)

    scene.open('api/routes/route_01.stexc')

    await asyncio.sleep(0.5)

    assert scene.path == 'api/routes/route_01.stexc'

    routes = scene.routes

    assert len(routes) == 1

    route = routes[0]

    assert len(route) == 5

    scene._detach()


@skip_when_no_server_running
async def test_scene_open_recording_misv01_accelerating_01(client):

    await clear_scene(client)

    scene = Scene()._attach(client)

    scene.open('api/recordings/misv01_accelerating_01.strec')

    await asyncio.sleep(0.5)

    assert scene.path == 'api/recordings/misv01_accelerating_01.strec'

    objects = scene.objects

    assert len(objects) == 1

    obj = objects[0]
    assert obj.code == 'misv01'

    scene._detach()



@skip_when_no_server_running
async def test_scene_add_route_01(client):

    scene = Scene()
    scene._attach(client)

    await load_scene(client, 'api/empty_nv.stexc')

    points = [
        [0.78059841735038,   0.6595292708678948],
        [0.7806435609656948, 0.6596289412962438],
        [0.7806108099163716, 0.6597198905621122],
        [0.7805305506012377, 0.6596962188353793],
        [0.7805034026243378, 0.6597311034853016],
        [0.7805034026243378, 0.6597311034853016]
    ]

    scene.routes.add("Test", points)

    test_scene = Scene() # need new test one to ensure route is created and available
    test_scene._attach(client)

    await asyncio.sleep(0.2)

    routes = scene.routes
    assert len(routes) == 1

    route = routes[0]
    assert route.uid == 1
    assert route.name == "Test"
    assert len(route) == 6

    routes = test_scene.routes
    assert len(routes) == 1

    route = routes[0]
    assert route.uid == 1
    assert route.name == "Test"
    assert len(route) == 6

    scene._detach()
    test_scene._detach()


@skip_when_no_server_running
async def test_scene_remove_route_01(client):

    scene = Scene()
    scene._attach(client)

    await load_scene(client, 'api/routes/route_01.stexc', delay = 0.5)

    route = scene.routes[0]
    assert len(route) == 5

    test_scene = Scene() # need new test one to ensure route is created and available
    test_scene._attach(client)

    scene.routes.remove(route)

    await asyncio.sleep(0.2)

    assert len(scene.routes) == 0
    assert len(test_scene.routes) == 0

    scene._detach()
    test_scene._detach()


@skip_when_no_server_running
async def test_scene_add_route_point_01(client):

    scene = Scene()
    scene._attach(client)

    await load_scene(client, 'api/routes/route_01.stexc', delay = 0.5)

    route = scene.routes[0]
    assert len(route) == 5

    test_scene = Scene() # need new test one to ensure route is created and available
    test_scene._attach(client)

    p = RoutePoint(
        name = "WP6",
        lat = 44.71945,
        lon = 37.802862,
    )

    route.append(p)

    await asyncio.sleep(0.1)

    route = scene.routes[0]
    assert route.uid == 1
    assert route.name == "Test route 1"
    assert len(route) == 6

    route = test_scene.routes[0]
    assert route.uid == 1
    assert route.name == "Test route 1"
    assert len(route) == 6

    point = route[-1]

    assert point.name == p.name
    assert point.type == p.type
    assert point.lat == pytest.approx(p.lat)
    assert point.lon == pytest.approx(p.lon)
    assert point.heading == p.heading
    assert point.velocity == p.velocity
    assert point.radius == p.radius

    scene._detach()
    test_scene._detach()


@skip_when_no_server_running
async def test_scene_insert_route_point_01(client):

    scene = Scene()
    scene._attach(client)

    await load_scene(client, 'api/routes/route_01.stexc', delay = 0.5)

    route = scene.routes[0]
    assert len(route) == 5
    point = route[2]
    assert point.name == "WP3"

    test_scene = Scene() # need new test one to ensure route is created and available
    test_scene._attach(client)

    p = RoutePoint(
        name = "WP-2-3",
        lat = 44.726658,
        lon = 37.796518,
    )

    route.insert(2, p)

    await asyncio.sleep(0.1)

    route = scene.routes[0]
    assert route.uid == 1
    assert route.name == "Test route 1"
    assert len(route) == 6

    route = test_scene.routes[0]
    assert route.uid == 1
    assert route.name == "Test route 1"
    assert len(route) == 6

    point = route[2]

    assert point.name == p.name
    assert point.type == p.type
    assert point.lat == pytest.approx(p.lat)
    assert point.lon == pytest.approx(p.lon)
    assert point.heading == p.heading
    assert point.velocity == p.velocity
    assert point.radius == p.radius

    scene._detach()
    test_scene._detach()


@skip_when_no_server_running
async def test_scene_remove_route_point_01(client):

    scene = Scene()
    scene._attach(client)

    await load_scene(client, 'api/routes/route_01.stexc', delay = 0.5)

    route = scene.routes[0]
    assert len(route) == 5

    test_scene = Scene() # need new test one to ensure route is created and available
    test_scene._attach(client)

    route.remove(3)

    await asyncio.sleep(0.1)

    route = scene.routes[0]
    assert route.uid == 1
    assert route.name == "Test route 1"
    assert len(route) == 4

    route = test_scene.routes[0]
    assert route.uid == 1
    assert route.name == "Test route 1"
    assert len(route) == 4


    scene._detach()
    test_scene._detach()


@skip_when_no_server_running
async def test_scene_change_route_point_01(client):

    scene = Scene()
    scene._attach(client)

    await load_scene(client, 'api/routes/route_01.stexc', delay = 0.5)

    route = scene.routes[0]
    assert len(route) == 5

    wp3 = route[2]
    assert wp3.name == "WP3"
    assert wp3.lat == pytest.approx(44.725705)
    assert wp3.lon == pytest.approx(37.799165)
    assert wp3.heading == 116.8
    assert wp3.velocity == pytest.approx(2.057777)
    assert wp3.radius == 200

    p_new = RoutePoint(
        name = "WP-Changed",
        lat = 44.726658,
        lon = 37.796518,
        heading = None,
        velocity = 1.5,
        radius = 300
    )

    route[2] = p_new

    test_scene = Scene() # need new test one to ensure route is created and available
    test_scene._attach(client)

    await asyncio.sleep(0.3)

    route = scene.routes[0]
    assert len(route) == 5

    wp = route[2]

    assert wp.name == p_new.name
    assert wp.lat == pytest.approx(p_new.lat)
    assert wp.lon == pytest.approx(p_new.lon)
    assert wp.heading == p_new.heading
    assert wp.velocity ==  p_new.velocity
    assert wp.radius == p_new.radius

    assert wp is wp3

    test_route = test_scene.routes[0]
    assert len(test_route) == 5
    assert not test_route is route

    wp = test_route[2]

    assert wp.name == p_new.name
    assert wp.lat == pytest.approx(p_new.lat)
    assert wp.lon == pytest.approx(p_new.lon)
    assert wp.heading == p_new.heading
    assert wp.velocity ==  p_new.velocity
    assert wp.radius == p_new.radius

    assert wp is not wp3

    scene._detach()
    test_scene._detach()


@skip_when_no_server_running
async def test_scene_change_route_point_02(client):

    scene = Scene()
    scene._attach(client)

    await load_scene(client, 'api/routes/route_01.stexc', delay = 0.5)

    route = scene.routes[0]
    assert len(route) == 5

    wp3 = route[2]
    assert wp3.name == "WP3"
    assert wp3.lat == pytest.approx(44.725705)
    assert wp3.lon == pytest.approx(37.799165)
    assert wp3.heading == 116.8
    assert wp3.velocity == pytest.approx(2.057777)
    assert wp3.radius == 200

    test_scene = Scene() # need new test one to ensure route is created and available
    test_scene._attach(client)

    wp3.name = "WP-Changed"
    wp3.lat = 44.726658
    wp3.lon = 37.796518
    wp3.heading = None
    wp3.velocity = 1.5
    wp3.radius = 300

    await asyncio.sleep(0.3)

    route = scene.routes[0]
    assert len(route) == 5

    wp = route[2]

    assert wp.name == wp3.name
    assert wp.lat == pytest.approx(wp3.lat)
    assert wp.lon == pytest.approx(wp3.lon)
    assert wp.heading == wp3.heading
    assert wp.velocity ==  wp3.velocity
    assert wp.radius == wp3.radius

    assert wp is wp3

    test_route = test_scene.routes[0]
    assert len(route) == 5

    wp = test_route[2]

    assert wp.name == wp3.name
    assert wp.lat == pytest.approx(wp3.lat)
    assert wp.lon == pytest.approx(wp3.lon)
    assert wp.heading == wp3.heading
    assert wp.velocity ==  wp3.velocity
    assert wp.radius == wp3.radius

    assert wp is not wp3

    scene._detach()
    test_scene._detach()


@skip_when_no_server_running
async def test_scene_open_api_objects_kbuoy01_01(client):

    await clear_scene(client)

    scene = Scene()
    scene._attach(client)

    scene.open('api/objects/kbuoy01_01.stexc')

    await asyncio.sleep(0.2)

    assert scene.path == 'api/objects/kbuoy01_01.stexc'

    objects = scene.objects

    assert len(objects) == 1

    o = objects[0]

    assert o.uid == 1
    assert o.code == "kbuoy01"
    assert o.name == "kbuoy01:1"

    o_code = objects["kbuoy01"]
    o_name = objects["kbuoy01:1"]

    assert o_code is o
    assert o_name is o

    assert o.pos == Vec3(20.0, 10.0, 0.0)
    assert o.quat == Quat(5.329889631866536e-7, 4.2835086588866037e-8, 0.5, -0.8660253882408142)

    geo = o.geo

    assert geo.lat == pytest.approx(0.0001798644)
    assert geo.lon == pytest.approx(-8.99322e-05)
    assert geo.alt == pytest.approx(0.0, abs=1e-4)

    eul = o.euler

    assert eul.heading == pytest.approx(-60.0)
    assert eul.pitch == pytest.approx(0.0, abs=1e-4)
    assert eul.roll == pytest.approx(0.0, abs=1e-4)

    assert o.linear == Vec3(0, 0, 0)
    assert o.angular == Vec3(0, 0, 0)

    assert not o.anchored
    assert o.cog == 0.0
    assert o.hdg == 60.0
    assert o.rot == 0.0
    assert o.sog == 0.0

    devices = o.devices

    assert len(devices) == 1

    vrs = devices[0]

    assert vrs.uid == 1
    assert vrs.path == "vrs.1"

    vrs_path = devices["vrs.1"]

    assert vrs_path is vrs

    assert vrs.heave == 0.0
    assert vrs.pitch == 0.0
    assert vrs.roll == 0.0

    scene._detach()



@skip_when_no_server_running
async def test_scene_open_api_objects_misv01_01(client):

    await clear_scene(client)

    scene = Scene()
    scene._attach(client)

    scene.open('api/objects/misv01_01.stexc')

    await asyncio.sleep(0.2)

    assert scene.path == 'api/objects/misv01_01.stexc'

    objects = scene.objects

    assert len(objects) == 1

    o = objects[0]

    assert o.uid == 1
    assert o.code == "misv01"
    assert o.name == "misv01:1"

    assert o.pos == Vec3(0.0, 0.0, -8.0)
    assert o.quat == Quat(0, 0, 0, -1)

    geo = o.geo

    assert geo.lat == pytest.approx(0.0)
    assert geo.lon == pytest.approx(0.0)
    assert geo.alt == pytest.approx(-8.0, abs=1e-8)

    eul = o.euler

    assert eul.heading == pytest.approx(0.0)
    assert eul.pitch == pytest.approx(0.0, abs=1e-4)
    assert eul.roll == pytest.approx(0.0, abs=1e-4)

    assert o.linear == Vec3(0, 0, 0)
    assert o.angular == Vec3(0, 0, 0)

    assert not o.anchored
    assert o.cog == 0.0
    assert o.hdg == 0.0
    assert o.rot == 0.0
    assert o.sog == 0.0

    devices = o.devices

    assert len(devices) == 62

    scene._detach()


@skip_when_no_server_running
async def test_scene_open_api_objects_misv01_set_throttle(client):

    await clear_scene(client)

    scene = Scene()
    scene._attach(client)

    scene.open('api/objects/misv01_01.stexc')

    await asyncio.sleep(0.2)

    assert scene.path == 'api/objects/misv01_01.stexc'

    misv = scene.objects['misv01']

    azipod_stbd = misv.devices["azipod.stbd"]

    azipod_stbd.throttle_order = 1.0

    for _ in range(20):
        client.send_request(RequestSimulationState.step())

    await asyncio.sleep(1.0)

    assert azipod_stbd.throttle_reply > 0.1

    scene._detach()


@skip_when_no_server_running
async def test_scene_open_api_objects_misv01_set_sog(client):

    await clear_scene(client)

    scene = Scene()
    scene._attach(client)

    scene.open('api/objects/misv01_01.stexc')

    await asyncio.sleep(0.2)

    misv = scene.objects['misv01']

    assert misv.sog == 0

    misv.sog = 5 # m/s

    for _ in range(10):
        client.send_request(RequestSimulationState.step())

    await asyncio.sleep(0.2)

    assert misv.sog < 5
    assert misv.sog > 4

    scene._detach()


@skip_when_no_server_running
async def test_scene_open_api_objects_misv01_set_cog(client):

    await clear_scene(client)

    scene = Scene()
    scene._attach(client)

    scene.open('api/objects/misv01_01.stexc')

    await asyncio.sleep(0.3)

    misv = scene.objects['misv01']

    assert misv.cog == 0

    misv.sog = 3 # setting cog only works if there's speed...
    misv.cog = 90 # degrees

    client.send_request(RequestSimulationState.step())
    client.send_request(RequestSimulationState.step())

    await asyncio.sleep(0.1)

    assert misv.cog == pytest.approx(90, abs=1E-2)

    assert misv.linear.equals(Vec3(0, -3, 0), abs = 0.1 )

    scene._detach()


@skip_when_no_server_running
async def test_scene_open_api_objects_misv01_set_linear_speed(client):

    await clear_scene(client)

    scene = Scene()
    scene._attach(client)

    scene.open('api/objects/misv01_01.stexc')

    await asyncio.sleep(0.3)

    misv = scene.objects['misv01']

    misv.linear = Vec3(10, 0, 0) # m/s

    for _ in range(10):
        client.send_request(RequestSimulationState.step())

    await asyncio.sleep(0.2)

    assert misv.sog < 10
    assert misv.sog > 9

    scene._detach()


