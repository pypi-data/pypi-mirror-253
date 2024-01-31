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

import math

from enum import Enum
from typing import Tuple, Optional, Union

from . euler import Euler, euler2quat, quat2euler
from . quat import Quat, Vec3


def dms2dd(d : int = 0,   # integer degrees
           m : int = 0,   # integer minutes
           s : float = 0, # decimal seconds
           _a = abs) -> float: # decimal degrees
    """
    Convert angle presented by (integer degrees, integer minutes, decimal seconds) to angle in decimal degrees.

    Args:
        d: Integer degrees.
        m: Integer minutes.
        s: Decimal seconds.

    Returns:
        dd: Angle in decimal degrees.
    """
    dd = _a(d) + _a(m)/60 + _a(s)/3600
    return dd if d >= 0 and m >= 0 and s >= 0 else -dd


def dd2dms(d : float = 0, # decimal degrees
           _f = math.floor,
           _a = abs) -> Tuple[int, int, float]: # (integer degrees, integer minutes, decimal seconds)
    """
    Convert angle presented by decimal degrees into angle in form of (integer degrees, integer minutes, decimal seconds).

    Args:
        d: Decimal degrees.

    Returns:
       (ideg, imin, dsec): Angle as tuple of (integer degrees, integer minutes, decimal seconds).
    """

    fdeg = _a(d)                # absolute value of decimal (float) degrees
    ideg = _f(fdeg)             # integer degrees
    fmin = _a(fdeg - ideg) * 60 # absolute value of float minutes
    imin = _f(fmin)             # integer minutes
    dsec = _a(fmin - imin) * 60 # decimal (float) seconds
    return (ideg, imin, dsec) if d >= 0 else (-ideg, -imin, -dsec)


def dd2ddm(d : float = 0,
           _dms = dd2dms,
           _a = abs) -> Tuple[int, float]: # decimal degrees -> to integer degrees + decimal minutes
    """
    Convert angle presented by Decimal Degrees (DD) into angle in form of Degrees Decimal Minutes (DDM) (integer degrees, decimal minutes).

    Args:
        d: Decimal degrees.

    Returns:
        (ideg, dmin): Angle as tuple of (integer degrees, decimal minutes).
    """
    ideg, imin, dsec = _dms(d)
    dmin = _a(imin) + _a(dsec) / 60
    return (ideg, dmin if d >= 0 else -dmin)


def ddm2dd(d : int = 0,
           dm : float = 0,
           _a = abs) -> float: # integer degrees + decimal minutes -> to decimal degrees
    """
    Convert angle presented by Degrees Decimal Minutes (DDM) (integer degrees, decimal minutes) into angle in Decimal Degrees (DD).

    Args:
        d: Integer degrees.
        dm: Decimal minutes.

    Returns:
        dd: Angle in decimal degrees.
    """
    dd = _a(d) + _a(dm) / 60
    return (dd if d >= 0 and dm >= 0 else -dd)


def dd2nmea(dd : float = 0,
            _dm = dd2ddm) -> float: # decimal degrees -> to NMEA(GPS)-like angle representation ddmm.mmmm
    """
    Convert angle presented by decimal degrees into NMEA-like angle representation (e.g. 51.507351 -> 5130.44106).

    Args:
        dd: Decimal degrees.

    Returns:
        n: Angle as used in NMEA protocol ddmm.mmmm.
    """
    ideg, dmin = _dm(dd)
    return ideg * 100 + dmin


def nmea2dd(n : float = 0,
            _f = math.floor,
            _a = abs,
            _dd = ddm2dd) -> float: # NMEA(GPS)-like angle representation ddmm.mmmm -> to decimal degrees
    """
    Convert angle given in NMEA(GPS)-like representation to decimal degrees (e.g. 5130.44106 -> 51.507351).

    Args:
        n: NMEA(GPS)-like angle value.

    Returns:
        d: Angle in decimal degrees.
    """
    fdeg = _a(n / 100.0)          # absolute value of decimal (float) degrees
    ideg = _f(fdeg)               # integer degrees
    fmin = _a(fdeg - ideg) * 100  # absolute value of float minutes
    dd = _dd(ideg, fmin)
    return dd if n >= 0 else -dd


dd_frmt = "%.8f\u00B0"
dm_frmt = "%d\u00B0%09.6f'"
dms_frmt = "%d\u00B00%d'%09.6f" + '"'
rad_frmt = "%.11f rad"

formats = [
    ('dd', "DEG", '''DEG: Decimal degrees, e.g. \u00B1''' + dd_frmt % 0.0, 'NONE', 1),
    ('dm', "DM",  '''DM: Integer degrees + decimal minutes, e.g. N ''' + dm_frmt % (0, 0), 'NONE', 2),
    ('dms', "DMS", '''DMS: Integer degrees + integer minutes + decimal seconds, e.g. N ''' + dms_frmt % (0, 0, 0), 'NONE', 4),
    ('rad', "RAD", '''RAD: Decimal radians, e.g. \u00B1''' + rad_frmt % 0.0, 'NONE', 8),
]


class CARDINAL(Enum):
    NORTH = 0
    SOUTH = 1
    EAST = 2
    WEST = 3

    @property
    def cap(self) -> str: # NORTH -> 'N', SOUTH -> 'S', EAST -> 'E', WEST -> 'W'
        return self.name[0]


class GeoPoint:

    __slots__ = 'lat', 'lon', 'alt'

    def __init__(self, lat=0, lon=0, alt=0): # lat/lon in decimal degrees, alt in meters
        self.lat = lat
        self.lon = lon
        self.alt = alt

    def __repr__(self):
        return f"GeoPoint({self.lat}, {self.lon}, {self.alt})"

    def __getitem__(self, idx):
        if idx == 0: return self.lat
        elif idx == 1: return self.lon
        elif idx == 2: return self.alt
        else: raise IndexError

    def __setitem__(self, idx, value):
        if idx == 0: self.lat = value
        elif idx == 1: self.lon = value
        elif idx == 2: self.alt = value
        else: raise IndexError

    @property
    def ns(self) -> str:
        return (CARDINAL.NORTH if self.lat >= 0 else CARDINAL.SOUTH).cap

    @property
    def ew(self) -> str:
        return (CARDINAL.EAST if self.lon >= 0 else CARDINAL.WEST).cap


EARTH_RADIUS = 6370997.0

QUAT_LTP = Quat().make_rotate(math.pi, Vec3(1, 0, 1))


def get_ltp_quat(geo: GeoPoint,
                 _q_ltp = QUAT_LTP,
                 _rad = math.radians) -> Quat:

    q_lat = Quat().make_rotate(-_rad(geo.lat), Vec3(0, 1, 0))
    q_lon = Quat().make_rotate(_rad(geo.lon), Vec3(0, 0, 1))

    return _q_ltp * q_lat * q_lon


def lla2ecef(geo: GeoPoint, eul: Optional[Euler] = None,
            _R = EARTH_RADIUS,
            _ltpq = get_ltp_quat,
            _eul2quat = euler2quat,
            _rad = math.radians,
            _sin = math.sin,
            _cos = math.cos) -> Union [Vec3, Tuple[Vec3, Quat]]:

    r = _R + geo.alt

    lat = _rad(geo[0])
    lon = _rad(geo[1])

    sin_lat = _sin(lat)
    sin_lon = _sin(lon)
    cos_lat = _cos(lat)
    cos_lon = _cos(lon)

    p_ecef = Vec3(r * cos_lon * cos_lat, r * cos_lat * sin_lon, r * sin_lat)

    if eul is None:
        return p_ecef

    q = _eul2quat(eul)
    q_ltp = _ltpq(geo)

    q_ecef = q * q_ltp

    return p_ecef, q_ecef


def ecef2lla(p: Vec3, q: Optional[Quat] = None,
             _R = EARTH_RADIUS,
             _eps = 1e-20,
            _ltpq = get_ltp_quat,
            _quat2euler = quat2euler,
            _abs = abs,
            _PI_2 = math.pi / 2,
            _deg = math.degrees,
            _asin = math.asin,
            _atan = math.atan2) -> Union[GeoPoint, Tuple[GeoPoint, Euler]]:

    _eps = 1e-20

    r = p.length()

    lat, lon = 0, 0
    lon = 0

    if _abs(r) > _eps:
        if _abs(p.x) < _eps and _abs(p.y) < _eps:
            lon = 0

            if p.z > 0:
                lat = _PI_2
            elif p.z < 0:
                lat = -_PI_2
        else:
            lat = _asin(p.z / r)
            lon = _atan(p.y, p.x)

    geo = GeoPoint(_deg(lat), _deg(lon), r - _R)

    if q is None:
        return geo

    q_ltp = _ltpq(geo)
    q_eul = q * q_ltp.inv

    eul = _quat2euler( q_eul )

    return geo, eul


def ecef2quat(p: GeoPoint,
              _ltpq = get_ltp_quat,
              _ecef2lla = ecef2lla):
    ''' Calculate quaternion of LTP using given position in ECEF '''
    return _ltpq(_ecef2lla(p))


def ecef2ltp(q: Quat, v: Vec3, w: Vec3):
    ''' Convert linear and angular speed vectors '''
    q_inv = q.inv
    v_ltp = q_inv * v
    w_ltp = q_inv * w
    return v_ltp, w_ltp
