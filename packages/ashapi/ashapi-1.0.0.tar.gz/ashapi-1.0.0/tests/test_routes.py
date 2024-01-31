import pytest, json

from conftest import get_data_path

from ashapi.route import Route, RoutePoint, PointType, route2json, route_from_config


def test_route_to_json():

    points = [
        RoutePoint("start#1", lat=44.69200, lon=37.793917, radius=10),
        RoutePoint("pause#1", lat=44.69227, lon=37.794352, radius=90, velocity=1.0289, type=PointType.STOP),
        RoutePoint(           lat=44.69342, lon=37.795890, radius=200, velocity=1.0289),
        RoutePoint(           lat=44.69329, lon=37.797888, radius=200, velocity=1.0289),
        RoutePoint("break#1", lat=44.69242, lon=37.814413, radius=200, velocity=4.63),
        RoutePoint("turn#1",  lat=44.69214, lon=37.819963, radius=200, velocity=1.4),
        RoutePoint("Target#1",lat=44.69212, lon=37.820348, radius=200, velocity=0.1, heading=321.0, type=PointType.STOP),
    ]

    route = Route("Test", points, objectid=13)

    jsstr = route2json(route)

    jsdict = json.loads(jsstr)

    with open(get_data_path("routes\\route02.json")) as f:
        expected = json.load(f)

    assert jsdict['name'] == expected['name']
    assert jsdict['objectid'] == expected['objectid']
    assert len(jsdict['points']) == len(expected['points'])

    for p, pexp in zip(jsdict['points'], expected['points']):
        assert p == pexp


def test_route_point_to_json():

    p = RoutePoint(lat = 44.71945, lon = 37.802862)

    msg1 = p.to_jstr()

    exp1 = '{"name": "", "velocity": 0.0, "radius": 0.0, "type": 1, "point": "4443.1670,N,03748.1717,E"}'

    assert msg1 == exp1

    msg2 = p.to_jstr(compact=True)

    exp2 = '{"name":"","velocity":0.0,"radius":0.0,"type":1,"point":"4443.1670,N,03748.1717,E"}'

    assert msg2 == exp2


def test_route_point_to_dict():

    p = RoutePoint(lat = 44.71945, lon = 37.802862)

    dic1 = p.to_dict()

    exp1 = {"name": "", "velocity": 0.0, "radius": 0.0, "type": 1, "point": "4443.1670,N,03748.1717,E"}

    assert dic1 == exp1

    dic2 = p.to_dict(only={'heading'})

    exp2 = {"point":"4443.1670,N,03748.1717,E"}

    assert dic2 == exp2

    p.heading = 22.8

    dic3 = p.to_dict(only={'heading'})

    exp3 = {"hdg":22.8, "point":"4443.1670,N,03748.1717,E"}

    assert dic3 == exp3


def test_route_point_from_dict():

    d = {"name":"WP4","velocity":1.2861111111111113,"radius":50.0,"type":1,"point":"4443.2664, N, 3747.8685, E"}

    p = RoutePoint.from_dict(d)

    assert p.name == "WP4"
    assert p.velocity == 1.2861111111111113
    assert p.radius == 50.0
    assert p.type == 1
    assert p.type == PointType.PASS
    assert p.lat == pytest.approx(44.721106)
    assert p.lon == pytest.approx(37.7978083)
    assert p.heading is None


    d = {"name":"WP3","velocity":2.057777777777778,"hdg":116.8,"radius":200.0,"type":1,"point":"4443.5423, N, 3747.9499, E"}

    p = RoutePoint.from_dict(d)

    assert p.name == "WP3"
    assert p.velocity == 2.057777777777778
    assert p.radius == 200.0
    assert p.type == 1
    assert p.type == PointType.PASS
    assert p.lat == pytest.approx(44.725705)
    assert p.lon == pytest.approx(37.799165)
    assert p.heading == 116.8


def test_route_from_config():

    route = route_from_config(get_data_path("routes\\route01.ini"))

    assert route.name == "AT-1-rndv"
    assert route.objectid is None
    assert len(route.points) == 7

    wp1 = route.points[0]

    assert wp1.name == r"start\d1"
    assert wp1.geo.lat == pytest.approx(44.69200)
    assert wp1.geo.lon == pytest.approx(37.793917)
    assert wp1.heading is None
    assert wp1.radius == 10
    assert wp1.velocity == 0.0
    assert wp1.type == PointType.PASS

    wp2 = route.points[1]

    assert wp2.name == r"pause\d1"
    assert wp2.geo.lat == pytest.approx(44.69227)
    assert wp2.geo.lon == pytest.approx(37.794352)
    assert wp2.heading is None
    assert wp2.radius == 90
    assert wp2.velocity == 1.0289
    assert wp2.type == PointType.STOP

    wp3 = route.points[2]

    assert wp3.name == ""
    assert wp3.geo.lat == pytest.approx(44.69342)
    assert wp3.geo.lon == pytest.approx(37.795890)
    assert wp3.heading is None
    assert wp3.radius == 200
    assert wp3.velocity == 1.0289
    assert wp3.type == PointType.PASS

    wp4 = route.points[3]

    assert wp4.name == ""
    assert wp4.geo.lat == pytest.approx(44.69329)
    assert wp4.geo.lon == pytest.approx(37.797888)
    assert wp4.heading is None
    assert wp4.radius == 200
    assert wp4.velocity == 1.0289
    assert wp4.type == PointType.PASS

    wp5 = route.points[4]

    assert wp5.name == r"break\d1"
    assert wp5.geo.lat == pytest.approx(44.69242)
    assert wp5.geo.lon == pytest.approx(37.814413)
    assert wp5.heading is None
    assert wp5.radius == 200
    assert wp5.velocity == 4.63
    assert wp5.type == PointType.PASS

    wp6 = route.points[5]

    assert wp6.name == r"turn\d1"
    assert wp6.geo.lat == pytest.approx(44.692145)
    assert wp6.geo.lon == pytest.approx(37.819963)
    assert wp6.heading is None
    assert wp6.radius == 200
    assert wp6.velocity == 1.4
    assert wp6.type == PointType.PASS

    wp7 = route.points[6]

    assert wp7.name == r"Target\d1"
    assert wp7.geo.lat == pytest.approx(44.69212)
    assert wp7.geo.lon == pytest.approx(37.820348)
    assert wp7.heading == 321.0
    assert wp7.radius == 200
    assert wp7.velocity == 0.1
    assert wp7.type == PointType.STOP


def test_route_index_access():

    route = route_from_config(get_data_path("routes\\route01.ini"))

    wp1 = route[0]

    assert wp1.name == r"start\d1"
    assert wp1 == route[r"start\d1"] # key access, by point name

    wp2 = route[1]

    assert wp2.name == r"pause\d1"
    assert wp2 == route[r"pause\d1"] # key access, by point name

    wp3 = route[2]

    assert wp3.name == ""
    assert wp3.geo.lat == pytest.approx(44.69342)
    assert wp3.geo.lon == pytest.approx(37.795890)
    assert wp3 == route[""] # key access, finds first by with name == ""

    wp4 = route[3]

    assert wp4.name == ""
    assert wp4.geo.lat == pytest.approx(44.69329)
    assert wp4.geo.lon == pytest.approx(37.797888)
    assert wp4 != route[""] # key access, route[""] == wp3

    wp5 = route[4]

    assert wp5.name == r"break\d1"
    assert wp5 == route[r"break\d1"] # key access, by point name

    wp6 = route[5]

    assert wp6.name == r"turn\d1"
    assert wp6 == route[r"turn\d1"] # key access, by point name

    wp7 = route[6]

    assert wp7.name == r"Target\d1"
    assert wp7 == route[r"Target\d1"] # key access, by point name

    pts = route[1:3]
    assert pts[0].name == r"pause\d1"
    assert pts[1].name == ""

    with pytest.raises(IndexError):
        wp = route[28]

    with pytest.raises(KeyError):
        wp = route["abcd"]


def test_route_index_assignment():

    route = route_from_config(get_data_path("routes\\route01.ini"))

    wp1 = route[0]
    wp7 = route[6]

    route[0] = RoutePoint("start#1", lat=44.69200, lon=37.793917, radius=10)

    route[-1] = RoutePoint("Target#1",lat=44.69212, lon=37.820348, radius=200, velocity=0.1, heading=321.0, type=PointType.STOP)

    wp1_ = route["start#1"]
    wp7_ = route["Target#1"]

    assert wp1 != wp1_
    assert wp7 != wp7_


def test_route_iteration():

    route = route_from_config(get_data_path("routes\\route01.ini"))

    names = [p.name for p in route]

    assert names == [r"start\d1", r"pause\d1", "", "", r"break\d1", r"turn\d1", r"Target\d1"]
