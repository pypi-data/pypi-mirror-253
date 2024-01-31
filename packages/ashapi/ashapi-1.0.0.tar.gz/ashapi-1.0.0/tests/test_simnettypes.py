import pytest

from ashapi.simnettypes import (
    NETTYPES,
    nettypes_factory,
    SimulationState,
    ObjectPositionOrder,
    AddRoute,
    RemoveRoute,
    ChangeRoute,
    AreaOrder,
    AreaOriginOrder,
    EnvironmentDepthOrder,
    EnvironmentTimeOrder,
    EnvironmentCurrentOrder,
    EnvironmentWindOrder,
    EnvironmentWaveOrder,
    EnvironmentTemperatureOrder,
    EnvironmentPrecipitationsOrder,
)


def test_all_nettypes():

    assert len(NETTYPES) == 35 # correct each time when new net-type is defined (and add assertion below)

    assert 'content-created'                in      NETTYPES
    assert 'content-deleted'                in      NETTYPES

    assert 'area'                           in      NETTYPES
    assert 'area-order'                     in      NETTYPES
    assert 'area-origin'                    in      NETTYPES
    assert 'area-origin-order'              in      NETTYPES

    assert 'environment-depth'                in      NETTYPES
    assert 'environment-depth-order'          in      NETTYPES
    assert 'environment-time'                 in      NETTYPES
    assert 'environment-time-order'           in      NETTYPES
    assert 'environment-temperature'          in      NETTYPES
    assert 'environment-temperature-order'    in      NETTYPES
    assert 'environment-wind'                 in      NETTYPES
    assert 'environment-wind-order'           in      NETTYPES
    assert 'environment-wave'                 in      NETTYPES
    assert 'environment-wave-order'           in      NETTYPES
    assert 'environment-current'              in      NETTYPES
    assert 'environment-current-order'        in      NETTYPES
    assert 'environment-weather-preset'       in      NETTYPES
    assert 'environment-precipitations'       in      NETTYPES
    assert 'environment-precipitations-order' in      NETTYPES

    assert 'add-object'                     in      NETTYPES
    assert 'add-object-with-offset'         in      NETTYPES
    assert 'object-added'                   in      NETTYPES
    assert 'object-data'                    in      NETTYPES
    assert 'object-position'                in      NETTYPES
    assert 'object-positionorder'           in      NETTYPES
    assert 'remove-object'                  in      NETTYPES
    assert 'object-removed'                 in      NETTYPES

    assert 'add-route'                      in      NETTYPES
    assert 'change-route'                   in      NETTYPES
    assert 'route'                          in      NETTYPES
    assert 'remove-route'                   in      NETTYPES
    assert 'route-removed'                  in      NETTYPES

    assert 'simulation-state'               in      NETTYPES


def test_ContentCreated_from_msg():

    msg = r'{"type":"content-created","json":"{\"path\":\"\"}"}'

    content_created = nettypes_factory(msg)

    assert isinstance(content_created, NETTYPES["content-created"])
    assert content_created.type == 'content-created'


def test_ContentDeleted_from_msg():

    msg = r'{"type":"content-deleted","json":"{}"}'

    content_deleted = nettypes_factory(msg)

    assert isinstance(content_deleted, NETTYPES["content-deleted"])
    assert content_deleted.type == 'content-deleted'


def test_AreaOrigin_from_msg():

    msg = r'{"type":"area-origin","json":"{\"lat\":0.78018661,\"lon\":0.6603453225}"}'

    ao = nettypes_factory(msg)

    assert isinstance(ao, NETTYPES["area-origin"])
    assert ao.type == 'area-origin'
    assert ao.lat == 0.78018661
    assert ao.lon == 0.6603453225


def test_AreaOriginOrder_to_msg():

    expected = '{"type":"area-origin-order","json":{"lat":0.32,"lon":0.51}}'

    ao = AreaOriginOrder(0.32, 0.51)

    msg = ao.to_jstr()
    assert msg == expected


{"type":"area-origin-order","json":"{\"lat\":0.32,\"lon\":0.51}"}

def test_Area_from_msg():

    msg = r'{"type":"area","json":"{\"name\":\"NV\",\"origo\":[0.78018661,0.6603453225],\"meshes\":[\"RU6MELN0.json\"],\"maps\":[\"RU4MDLM0.xml\",\"RU5MELN0.xml\",\"RU6MELN1.xml\",\"RU6MELN0.xml\"]}"}'

    area = nettypes_factory(msg)

    assert isinstance(area, NETTYPES["area"])
    assert area.type == 'area'
    assert area.name == "NV"
    assert area.origo == [0.78018661, 0.6603453225]
    assert area.meshes == ["RU6MELN0.json"]
    assert area.maps == ["RU4MDLM0.xml", "RU5MELN0.xml", "RU6MELN1.xml", "RU6MELN0.xml"]


def test_AreaOrder_to_msg():

    # minimal required

    ao = AreaOrder(
        name = "NV",
        origo = [0.78018661,0.6603453225],
        meshes = [],
        maps = []
    )

    msg = ao.to_jstr()

    expected = r'{"type":"area-order","json":{"name":"NV","origo":[0.78018661,0.6603453225],"meshes":[],"maps":[]}}'

    assert msg == expected

    # also possible

    ao = AreaOrder(
        name = "NV",
        title = "",
        description = [],
        origo = [0.78018661,0.6603453225],
        meshes = ["RU6MELN0.json"],
        maps = ["RU4MDLM0.xml", "RU5MELN0.xml", "RU6MELN1.xml", "RU6MELN0.xml"]
    )

    msg = ao.to_jstr()

    expected = r'{"type":"area-order","json":{"name":"NV","title":"","description":[],"origo":[0.78018661,0.6603453225],"meshes":["RU6MELN0.json"],"maps":["RU4MDLM0.xml","RU5MELN0.xml","RU6MELN1.xml","RU6MELN0.xml"]}}'

    assert msg == expected

    # full with title and description

    # TODO: check the bullshit with enconding
    #
    # ao = AreaOrder(
    #     name = "NV",
    #     title = "Порт Новороссийск",
    #     description = ["Порт", "Новороссийск"],
    #     origo = [0.78018661,0.6603453225],
    #     meshes = ["RU6MELN0.json"],
    #     maps = ["RU4MDLM0.xml", "RU5MELN0.xml", "RU6MELN1.xml", "RU6MELN0.xml"]
    # )

    # msg = ao.to_jstr()

    # expected = r'{"type":"area-order","json":{"name":"NV","title":"Порт Новороссийск","description":["Порт", "Новороссийск"],"origo":[0.78018661,0.6603453225],"meshes":["RU6MELN0.json"],"maps":["RU4MDLM0.xml","RU5MELN0.xml","RU6MELN1.xml","RU6MELN0.xml"]}}'

    # assert msg == expected


def test_EnvironmentDepth_from_msg():

    msg = r'{"type":"environment-depth","json":"{\"depth\":33.0}"}'

    depth = nettypes_factory(msg)

    assert isinstance(depth, NETTYPES["environment-depth"])
    assert depth.type == 'environment-depth'
    assert depth.depth == 33.0


def test_EnvironmentDepthOrder_to_msg():

    expected = '{"type":"environment-depth-order","json":{"depth":33.0}}'

    env = EnvironmentDepthOrder(33.0)

    msg = env.to_jstr()

    assert msg == expected


def test_EnvironmentTemperature_from_msg():

    msg = r'{"type":"environment-temperature","json":"{\"air\":25.0,\"water\":21.0}"}'

    temp = nettypes_factory(msg)

    assert isinstance(temp, NETTYPES["environment-temperature"])
    assert temp.type == 'environment-temperature'
    assert temp.air == 25.0
    assert temp.water == 21.0


def test_EnvironmentTemperatureOrder_to_msg():

    expected = '{"type":"environment-temperature-order","json":{"air":32.0,"water":24.0}}'

    env = EnvironmentTemperatureOrder(32.0, 24.0)

    msg = env.to_jstr()

    assert msg == expected


def test_EnvironmentTime_from_msg():

    msg = r'{"type":"environment-time","json":"{\"time\":1702624835}"}'

    etime = nettypes_factory(msg)

    assert isinstance(etime, NETTYPES["environment-time"])
    assert etime.type == 'environment-time'
    assert etime.time == 1702624835


def test_EnvironmentTimeOrder_to_msg():

    expected = '{"type":"environment-time-order","json":{"time":1702624835}}'

    env = EnvironmentTimeOrder(1702624835)

    msg = env.to_jstr()

    assert msg == expected



def test_EnvironmentWind_from_msg():

    msg = r'{"type":"environment-wind","json":"{\"direction_from\":0.5235987755982988,\"speed\":5.144444444444445}"}'

    wind = nettypes_factory(msg)

    assert isinstance(wind, NETTYPES["environment-wind"])
    assert wind.type == 'environment-wind'
    assert wind.direction_from == 0.5235987755982988
    assert wind.speed == 5.144444444444445


def test_EnvironmentWindOrder_to_msg():

    expected = '{"type":"environment-wind-order","json":{"direction_from":3.14,"speed":10.0}}'

    env = EnvironmentWindOrder(3.14, 10.0)

    msg = env.to_jstr()

    assert msg == expected


def test_EnvironmentCurrent_from_msg():

    msg = r'{"type":"environment-current","json":"{\"direction_to\":3.490658503988659,\"speed\":2.5722222222222226}"}'

    curr = nettypes_factory(msg)

    assert isinstance(curr, NETTYPES["environment-current"])
    assert curr.type == 'environment-current'
    assert curr.direction_to == 3.490658503988659
    assert curr.speed == 2.5722222222222226


def test_EnvironmentCurrentOrder_to_msg():

    expected = '{"type":"environment-current-order","json":{"direction_to":1.57,"speed":2.0}}'

    env = EnvironmentCurrentOrder(1.57, 2.0)

    msg = env.to_jstr()

    assert msg == expected


def test_EnvironmentWave_from_msg():

    msg = r'{"type":"environment-wave","json":"{\"direction_to\":3.7524578917878088,\"wind_speed\":9.442000058608136,\"typical_height\":2.0,\"typical_length\":53.8,\"direction_spread\":0.5235987755982988,\"number_of_frequencies\":15,\"number_of_directions\":11}"}'

    wave = nettypes_factory(msg)

    assert isinstance(wave, NETTYPES["environment-wave"])
    assert wave.type == 'environment-wave'
    assert wave.direction_to == 3.7524578917878088
    assert wave.wind_speed == 9.442000058608136
    assert wave.typical_height == 2.0
    assert wave.typical_length == 53.8
    assert wave.direction_spread == 0.5235987755982988
    assert wave.number_of_frequencies == 15
    assert wave.number_of_directions == 11


def test_EnvironmentWaveOrder_to_msg():

    expected = '{"type":"environment-wave-order","json":{"direction_to":0.3490658503988659,"wind_speed":0,"typical_height":2,"typical_length":53.8,"direction_spread":0.5235987755982988,"number_of_frequencies":9,"number_of_directions":11}}'

    env = EnvironmentWaveOrder(
        direction_to = 0.3490658503988659,
        # wind_speed = 0,
        typical_height = 2,
        typical_length = 53.8,
        direction_spread = 0.5235987755982988,
        number_of_frequencies = 9,
        number_of_directions = 11
    )

    msg = env.to_jstr()

    assert msg == expected



def test_EnvironmentWeatherPreset_from_msg():

    msg = r'{"type":"environment-weather-preset","json":"{\"preset\":7}"}'

    preset = nettypes_factory(msg)

    assert isinstance(preset, NETTYPES["environment-weather-preset"])
    assert preset.type == 'environment-weather-preset'
    assert preset.preset == 7


def test_EnvironmentPrecipitations_from_msg():

    msg = r'{"type":"environment-precipitations","json":"{\"fog\":0.2,\"clouds\":0.5,\"rain\":0.3,\"snow\":0.1}"}'

    prec = nettypes_factory(msg)

    assert isinstance(prec, NETTYPES["environment-precipitations"])
    assert prec.type == 'environment-precipitations'
    assert prec.fog == 0.2
    assert prec.clouds == 0.5
    assert prec.rain == 0.3
    assert prec.snow == 0.1


def test_EnvironmentPrecipitationsOrder_to_msg():

    expected = r'{"type":"environment-precipitations-order","json":{"fog":0.2,"clouds":0.5,"rain":0.3,"snow":0.1}}'

    env = EnvironmentPrecipitationsOrder(fog=0.2, clouds=0.5, rain=0.3, snow=0.1)

    msg = env.to_jstr()

    assert msg == expected


SimulationState_from_msg_test_data = [
    (
        r'{"type":"simulation-state","json":"{\"running\":false,\"playback\":false,\"recording\":false,\"created\":false,\"duration\":0,\"start\":0,\"time\":0,\"ticks\":0,\"accel\":1,\"maxaccel\":false,\"realaccel\":1}"}', 
        SimulationState()
    ),
    (
        r'{"type":"simulation-state","json":"{\"running\":true,\"playback\":false,\"recording\":false,\"created\":false,\"duration\":0,\"start\":0,\"time\":0,\"ticks\":2,\"accel\":1,\"maxaccel\":false,\"realaccel\":1}"}', 
        SimulationState(running=True, ticks=2)
    )
]

@pytest.mark.parametrize("msg, simstate_expected", SimulationState_from_msg_test_data)
def test_SimulationState_from_msg(msg, simstate_expected):

    simstate = nettypes_factory(msg)

    assert isinstance(simstate, SimulationState)
    assert simstate.type == 'simulation-state'
    assert simstate == simstate_expected


# 

def test_AddObject_from_msg():

    msg = r'{"type":"add-object","json":"{\"code\":\"cargo01\",\"name\":\"Bulker\",\"globalPose\":[-6.337593937292695,-4.266403745466586,-3.740004579536617],\"globalOrientation\":[-5.008371382342336e-7,3.296349335712989e-7,0.3859113819934591,-0.9225358558059079],\"linearVelocity\":[0,0,0],\"angularVelocity\":[0,0,0]}"}'

    add = nettypes_factory(msg)

    assert isinstance(add,  NETTYPES["add-object"])
    assert add.type == 'add-object'

    assert add.code == "cargo01"
    assert add.name == "Bulker"
    assert add.globalPose == [-6.337593937292695,-4.266403745466586,-3.740004579536617]
    assert add.globalOrientation == [-5.008371382342336e-7,3.296349335712989e-7,0.3859113819934591,-0.9225358558059079]
    assert add.linearVelocity == [0.0,0.0,0.0]
    assert add.angularVelocity == [0.0,0.0,0.0]


def test_ObjectAdded_from_msg():

    msg = r'{"type":"object-added","json":"{\"objectId\":1,\"code\":\"kbuoy01\",\"name\":\"kbuoy01:1\"}"}'

    obj = nettypes_factory(msg)

    assert isinstance(obj,  NETTYPES["object-added"])
    assert obj.type == 'object-added'

    assert obj.objectId == 1
    assert obj.code == "kbuoy01"
    assert obj.name == "kbuoy01:1"



def test_ObjectData_from_msg():

    msg = r'{"type":"object-data","json":"{\"objectId\":1,\"group\":\"physics\",\"path\":\"\",\"values\":[{\"anchored\":0.0},{\"cog\":0.0},{\"hdg\":60.0},{\"rot\":0.0},{\"sog\":0.0}]}"}'

    odata = nettypes_factory(msg)

    assert isinstance(odata,  NETTYPES["object-data"])
    assert odata.type == 'object-data'

    assert odata.objectId == 1
    assert odata.group == "physics"
    assert odata.path == ""
    assert odata.values == [
        {"anchored": 0.0},
        {"cog": 0.0},
        {"hdg": 60.0},
        {"rot": 0.0},
        {"sog":0.0}
    ]

    msg = r'{"type":"object-data","json":"{\"objectId\":1,\"group\":\"physics\",\"path\":\"gps.2(stbd)\",\"values\":[{\"lat\":0.000285988781},{\"lon\":0.00004223315}]}"}'

    odata = nettypes_factory(msg)

    assert isinstance(odata,  NETTYPES["object-data"])
    assert odata.type == 'object-data'

    assert odata.objectId == 1
    assert odata.group == "physics"
    assert odata.path == "gps.2(stbd)"
    assert odata.values == [
        {"lat": 0.000285988781},
        {"lon": 0.00004223315},
    ]


def test_RemoveObject_from_msg():

    msg = r'{"type":"remove-object","json":"{\"objectId\":1}"}'

    rm = nettypes_factory(msg)

    assert isinstance(rm,  NETTYPES["remove-object"])
    assert rm.type == 'remove-object'

    assert rm.objectId == 1


def test_ObjectRemoved_from_msg():

    msg = r'{"type":"object-removed","json":"{\"objectId\":1}"}'

    rem = nettypes_factory(msg)

    assert isinstance(rem,  NETTYPES["object-removed"])
    assert rem.type == 'object-removed'

    assert rem.objectId == 1



def test_ObjectPosition_from_msg():

    msg = r'{"type":"object-position","json":"{\"objectId\":1,\"globalPose\":[11.618515968322754,39.608123779296878,-0.0001337137073278427],\"globalOrientation\":[0.000003223926569262403,3.167444617702131e-7,0.3739517629146576,-0.9274482727050781],\"linearVelocity\":[0.0,0.0,0.0],\"angularVelocity\":[0.0,0.0,0.0]}"}'

    object_position = nettypes_factory(msg)

    assert isinstance(object_position,  NETTYPES["object-position"])
    assert object_position.type == 'object-position'

    assert object_position.objectId == 1
    assert object_position.globalPose == [11.618515968322754,39.608123779296878,-0.0001337137073278427]
    assert object_position.globalOrientation == [0.000003223926569262403,3.167444617702131e-7,0.3739517629146576,-0.9274482727050781]
    assert object_position.linearVelocity == [0.0,0.0,0.0]
    assert object_position.angularVelocity == [0.0,0.0,0.0]


# @TODO: this is really quite strange, that msg_str for nettype coming from websocket differs from jstr generated from nettype.
# @TODO: For example here '"json":"{...}"' (coming from websocket, see above `test_ObjectPosition_from_msg`)
# @TODO: For example here '"json":{...}' (generated by nettype, see below, `test_ObjectPositionOrder_to_jstr`)
# @TODO: But practice shows that otherwise ObjectPositionOrder is not working when sent to server
def test_ObjectPositionOrder_to_msg():

    order = ObjectPositionOrder(1, [50,100,0], [0,0,0,1], [0.0,0.0,0.0], [0.0,0.0,0.0])
    jstr = order.to_jstr()

    expected = r'{"type":"object-positionorder","json":{"objectId":1,"globalPose":[50,100,0],"globalOrientation":[0,0,0,1],"linearVelocity":[0.0,0.0,0.0],"angularVelocity":[0.0,0.0,0.0]}}'

    assert jstr == expected


def test_AddRoute_from_msg():

    msg = r'{"type":"add-route","json":"{\"name\":\"\",\"points\":[[0.78059841735038,0.6595292708678948],[0.7806435609656948,0.6596289412962438],[0.7806108099163716,0.6597198905621122],[0.7805305506012377,0.6596962188353793],[0.7805034026243378,0.6597311034853016],[0.7805034026243378,0.6597311034853016]]}"}'

    add = nettypes_factory(msg)

    assert isinstance(add,  NETTYPES["add-route"])
    assert add.type == 'add-route'

    assert add.name == ""
    assert add.points == [
        [0.78059841735038, 0.6595292708678948],
        [0.7806435609656948, 0.6596289412962438],
        [0.7806108099163716, 0.6597198905621122],
        [0.7805305506012377, 0.6596962188353793],
        [0.7805034026243378, 0.6597311034853016],
        [0.7805034026243378, 0.6597311034853016]
    ]

def test_AddRoute_to_msg():

    add = AddRoute(
        points = [
            [0.78059841735038, 0.6595292708678948],
            [0.7806435609656948, 0.6596289412962438],
            [0.7806108099163716, 0.6597198905621122],
            [0.7805305506012377, 0.6596962188353793],
            [0.7805034026243378, 0.6597311034853016],
            [0.7805034026243378, 0.6597311034853016]
        ]
    )

    msg = add.to_jstr()

    expected = r'{"type":"add-route","json":{"name":"","points":[[0.78059841735038,0.6595292708678948],[0.7806435609656948,0.6596289412962438],[0.7806108099163716,0.6597198905621122],[0.7805305506012377,0.6596962188353793],[0.7805034026243378,0.6597311034853016],[0.7805034026243378,0.6597311034853016]]}}'

    assert msg == expected


def test_ChangeRoute_name_from_msg():

    msg = r'{"type":"change-route","json":"{\"objectid\":1,\"name\":\"Test route 1\"}"}'

    change = nettypes_factory(msg)

    assert isinstance(change,  NETTYPES["change-route"])
    assert change.type == 'change-route'

    assert change.objectid == 1
    assert change.name == "Test route 1"
    assert change.changed is None
    assert change.removed is None


def test_ChangeRoute_point_type_from_msg():

    msg = r'{"type":"change-route","json":"{\"objectid\":13,\"name\":\"Some route\",\"changed\":{\"index\":2,\"point\":{\"name\":\"\",\"type\":1,\"point\":\"4443.5423,N,03747.9499,E\"}}}"}'

    change = nettypes_factory(msg)

    assert isinstance(change,  NETTYPES["change-route"])
    assert change.type == 'change-route'

    assert change.objectid == 13
    assert change.name == "Some route"
    assert change.changed == {
        "index": 2,
        "point": {
            "name": "",
            "type": 1,
            "point": "4443.5423,N,03747.9499,E"
        }
    }
    assert change.removed is None


def test_ChangeRoute_point_velocity_from_msg():

    msg = r'{"type":"change-route","json":"{\"objectid\":1,\"name\":\"Test name\",\"changed\":{\"index\":3,\"point\":{\"name\":\"\",\"type\":0,\"point\":\"4443.3555,N,03747.9589,E\",\"velocity\":2.5722222222222224}}}"}'

    change = nettypes_factory(msg)

    assert isinstance(change,  NETTYPES["change-route"])
    assert change.type == 'change-route'

    assert change.objectid == 1
    assert change.name == "Test name"
    assert change.changed == {
        "index": 3,
        "point": {
            "name": "",
            "type": 0,
            "point": "4443.3555,N,03747.9589,E",
            "velocity": 2.5722222222222224
        }
    }
    assert change.removed is None


def test_ChangeRoute_point_radius_from_msg():

    msg = r'{"type":"change-route","json":"{\"objectid\":1,\"name\":\"Test name\",\"changed\":{\"index\":4,\"point\":{\"name\":\"\",\"type\":0,\"point\":\"4443.2685,N,03747.9812,E\",\"radius\":200}}}"}'

    change = nettypes_factory(msg)

    assert isinstance(change,  NETTYPES["change-route"])
    assert change.type == 'change-route'

    assert change.objectid == 1
    assert change.name == "Test name"
    assert change.changed == {
        "index": 4,
        "point": {
            "name": "",
            "type": 0,
            "point": "4443.2685,N,03747.9812,E",
            "radius": 200
        }
    }
    assert change.removed is None


def test_ChangeRoute_point_heading_from_msg():

    msg = r'{"type":"change-route","json":"{\"objectid\":1,\"name\":\"Test name\",\"changed\":{\"index\":0,\"point\":{\"name\":\"\",\"type\":0,\"point\":\"4443.5126,N,03747.1820,E\",\"hdg\":10}}}"}'

    change = nettypes_factory(msg)

    assert isinstance(change,  NETTYPES["change-route"])
    assert change.type == 'change-route'

    assert change.objectid == 1
    assert change.name == "Test name"
    assert change.changed == {
        "index": 0,
        "point": {
            "name": "",
            "type": 0,
            "point": "4443.5126,N,03747.1820,E",
            "hdg": 10
        }
    }
    assert change.removed is None


def test_ChangeRoute_point_from_msg():

    msg = r'{"type":"change-route","json":"{\"objectid\":1,\"name\":\"Test route 1\",\"changed\":{\"index\":2,\"point\":{\"name\":\"WP3\",\"velocity\":2.057777777777778,\"hdg\":116.8,\"radius\":200,\"type\":1,\"point\":\"4443.6286,N,03748.0888,E\"}}}"}'

    change = nettypes_factory(msg)

    assert isinstance(change,  NETTYPES["change-route"])
    assert change.type == 'change-route'

    assert change.objectid == 1
    assert change.name == "Test route 1"
    assert change.changed == {
        "index": 2,
        "point": {
            "name": "WP3",
            "type": 1,
            "point": "4443.6286,N,03748.0888,E",
            "velocity": 2.057777777777778,
            "hdg": 116.8,
            "radius": 200
        }
    }
    assert change.removed is None


def test_ChangeRoute_added_point_to_msg():

    ch = ChangeRoute(
        id = 1,
        name = "Test route 1",
        added = {
            "index": 5,
            "point": {"point": "4443.1642,N,03748.1276,E"}
        })

    msg = ch.to_jstr()
    exp = '{"type":"change-route","json":{"objectid":1,"name":"Test route 1","added":{"index":5,"point":{"point":"4443.1642,N,03748.1276,E"}}}}'

    assert msg == exp


def test_Route_from_msg():

    msg =  r'{"type":"route","json":"{\"objectid\":1,\"name\":\"Test route 1\",'
    msg += r'\"points\":['
    msg += r'{\"name\":\"WP1\",\"type\":1,\"point\":\"4443.4997, N, 3747.2946, E\"},'
    msg += r'{\"name\":\"WP2\",\"velocity\":2.5722222222222226,\"hdg\":57.400000000000009,\"radius\":250.0,\"type\":1,\"point\":\"4443.6549, N, 3747.6373, E\"},'
    msg += r'{\"name\":\"WP3\",\"velocity\":2.057777777777778,\"hdg\":116.8,\"radius\":200.0,\"type\":1,\"point\":\"4443.6286, N, 3748.0888, E\"},'
    msg += r'{\"name\":\"WP4\",\"velocity\":1.2861111111111113,\"radius\":50.0,\"type\":1,\"point\":\"4443.2664, N, 3747.8685, E\"},'
    msg += r'{\"name\":\"WP5-STOP\",\"type\":0,\"point\":\"4443.1731, N, 3747.9885, E\"}]}"}'

    route = nettypes_factory(msg)

    assert isinstance(route,  NETTYPES["route"])
    assert route.type == 'route'

    assert route.objectid == 1
    assert route.name == "Test route 1"

    assert len(route.points) == 5

    assert route.points[0] == {
        "name": "WP1",
        "type": 1,
        "point": "4443.4997, N, 3747.2946, E",
    }

    assert route.points[1] == {
        "name": "WP2",
        "type": 1,
        "point": "4443.6549, N, 3747.6373, E",
        "velocity": 2.5722222222222226,
        "hdg": 57.400000000000009,
        "radius": 250.0
    }

    assert route.points[2] == {
        "name": "WP3",
        "type": 1,
        "point": "4443.6286, N, 3748.0888, E",
        "velocity": 2.057777777777778,
        "hdg": 116.8,
        "radius": 200.0
    }

    assert route.points[3] == {
        "name": "WP4",
        "type": 1,
        "point": "4443.2664, N, 3747.8685, E",
        "velocity": 1.2861111111111113,
        "radius": 50.0
    }

    assert route.points[4] == {
        "name": "WP5-STOP",
        "type": 0,
        "point": "4443.1731, N, 3747.9885, E",
    }


def test_RemoveRoute_from_msg():

    msg = r'{"type":"remove-route","json":"{\"objectid\":1}"}'

    rm = nettypes_factory(msg)

    assert isinstance(rm,  NETTYPES["remove-route"])
    assert rm.type == 'remove-route'

    assert rm.objectid == 1


def test_RemoveRoute_to_msg():

    rm = RemoveRoute(1)

    msg = rm.to_jstr()

    exp = r'{"type":"remove-route","json":{"objectid":1}}'

    assert msg == exp


def test_RouteRemoved_from_msg():

    msg = r'{"type":"route-removed","json":"{\"objectid\":1}"}'

    rem = nettypes_factory(msg)

    assert isinstance(rem,  NETTYPES["route-removed"])
    assert rem.type == 'route-removed'

    assert rem.objectid == 1
