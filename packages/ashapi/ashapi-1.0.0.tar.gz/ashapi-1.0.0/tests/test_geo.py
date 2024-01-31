import pytest

from ashapi.geo import GeoPoint, CARDINAL, dms2dd, dd2dms, dd2ddm, ddm2dd, dd2nmea, nmea2dd


geo_saint_petersburg = GeoPoint(59.93863, 30.31413) # Saint-Petersburg, Russia
geo_san_francisco = GeoPoint(37.77493, -122.41942) # San Francisco, USA
geo_sydney = GeoPoint(-33.8559799094, 151.20666584) # Sydney, Australia
geo_buenos_aires = GeoPoint(-34.61315, -58.37723) # Buenos Aires, Argentina


def test_geopoint_construction():

    geo = GeoPoint()

    assert geo.lat == 0
    assert geo.lon == 0

    assert geo_saint_petersburg.lat == 59.93863
    assert geo_saint_petersburg.lon == 30.31413

    assert geo_san_francisco.lat == 37.77493
    assert geo_san_francisco.lon == -122.41942

    assert geo_sydney.lat == -33.8559799094
    assert geo_sydney.lon == 151.20666584

    assert geo_buenos_aires.lat == -34.61315
    assert geo_buenos_aires.lon == -58.37723


def test_geopoint_indexget():

    geo = GeoPoint(59.93863, 30.31413, 5.328)

    assert geo[0] == geo.lat
    assert geo[1] == geo.lon
    assert geo[2] == geo.alt

    with pytest.raises(IndexError):
        _ = geo[3]


def test_geopoint_indexset():

    geo = GeoPoint() # 59.93863, 30.31413, 5.328)

    geo[0] = 59.93863
    geo[1] = 30.31413
    geo[2] = 5.328

    assert geo.lat == 59.93863
    assert geo.lon == 30.31413
    assert geo.alt ==  5.328

    with pytest.raises(IndexError):
        geo[3] = 3.14


def test_geopoint_cardinal():

    assert geo_saint_petersburg.ns == 'N'
    assert geo_saint_petersburg.ew == 'E'

    assert geo_san_francisco.ns == 'N'
    assert geo_san_francisco.ew == 'W'

    assert geo_sydney.ns == 'S'
    assert geo_sydney.ew == 'E'

    assert geo_buenos_aires.ns == 'S'
    assert geo_buenos_aires.ew == 'W'


def test_geo_cardinal():

    assert CARDINAL.NORTH.cap == 'N'
    assert CARDINAL.SOUTH.cap == 'S'
    assert CARDINAL.EAST.cap == 'E'
    assert CARDINAL.WEST.cap == 'W'


def test_dd_to_dms():

    d, m, s = dd2dms(0)

    assert d == 0
    assert m == 0
    assert s == pytest.approx(0)

    d, m, s = dd2dms(59.93863)

    assert d == 59
    assert m == 56
    assert s == pytest.approx(19.068)

    d, m, s = dd2dms(30.31413)

    assert d == 30
    assert m == 18
    assert s == pytest.approx(50.868)

    d, m, s = dd2dms(-122.41942)

    assert d == -122
    assert m == -25
    assert s == pytest.approx(-9.912)

    d, m, s = dd2dms(-33.8559799094)

    assert d == -33
    assert m == -51
    assert s == pytest.approx(-21.52767)

    d, m, s = dd2dms(151.206665844)

    assert d == 151
    assert m == 12
    assert s == pytest.approx(23.99704)

    d, m, s = dd2dms(-58.37723)

    assert d == -58
    assert m == -22
    assert s == pytest.approx(-38.02799)


def test_dms_to_dd():

    d = dms2dd(0, 0, 0)

    assert d == 0

    d = dms2dd(59, 56, 19.068)

    assert d == pytest.approx(59.93863)

    d = dms2dd(30, 18, 50.868)

    assert d == pytest.approx(30.31413)

    d = dms2dd(-122, -25, -9.912)

    assert d == pytest.approx(-122.41942)

    d = dms2dd(-33, -51, -21.52767)

    assert d == pytest.approx(-33.8559799094)

    d = dms2dd(151, 12, 23.99704)

    assert d == pytest.approx(151.206665844)

    d = dms2dd(-58, -22, -38.02799)

    assert d == pytest.approx(-58.37723)


def test_dd_to_ddm():

    d, m = dd2ddm(0)

    assert d == 0
    assert m == pytest.approx(0)

    d, m = dd2ddm(59.93863)

    assert d == 59
    assert m == pytest.approx(56.3178)

    d, m = dd2ddm(30.31413)

    assert d == 30
    assert m == pytest.approx(18.8478)

    d, m = dd2ddm(-122.41942)

    assert d == -122
    assert m == pytest.approx(-25.1652)

    d, m = dd2ddm(-33.8559799094)

    assert d == -33
    assert m == pytest.approx(-51.358794)

    d, m = dd2ddm(151.206665844)

    assert d == 151
    assert m == pytest.approx(12.39995)

    d, m = dd2ddm(-58.37723)

    assert d == -58
    assert m == pytest.approx(-22.6338)


def test_ddm_to_dd():

    dd = ddm2dd(0, 0)

    assert dd == 0

    dd = ddm2dd(59, 56.3178)

    assert dd == pytest.approx(59.93863)

    dd = ddm2dd(30, 18.8478)

    assert dd == pytest.approx(30.31413)

    dd = ddm2dd(-122, -25.1652)

    assert dd == pytest.approx(-122.41942)

    dd = ddm2dd(-33, -51.358794)

    assert dd == pytest.approx(-33.8559799094)

    dd = ddm2dd(151, 12.39995)

    assert dd == pytest.approx(151.206665844)

    dd = ddm2dd(-58, -22.6338)

    assert dd == pytest.approx(-58.37723)


nmea2deg = [
    (0, 0),
    (5956.3178, 59.93863),
    (3018.8478, 30.31413),
    (-12225.1652, -122.41942),
    (-3351.358794, -33.8559799094),
    (15112.39995, 151.206665844),
    (-5822.6338, -58.37723),
    (4443.1670, 44.71945),
    (3748.1717, 37.802862),
    (4443.5995, 44.726658),
    (3747.7911, 37.796518),
]

deg2nmea = [(d, n) for n, d in nmea2deg]


@pytest.mark.parametrize("angle_deg, angle_gps", deg2nmea)
def test_dd_to_nmea(angle_deg, angle_gps):

    d = dd2nmea(angle_deg)

    assert d == pytest.approx(angle_gps)


@pytest.mark.parametrize("angle_gps, angle_deg", nmea2deg)
def test_nmea_to_dd(angle_gps, angle_deg):

    d = nmea2dd(angle_gps)

    assert d == pytest.approx(angle_deg)
