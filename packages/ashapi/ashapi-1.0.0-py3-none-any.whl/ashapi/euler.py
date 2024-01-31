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

from . quat import Quat, is_number


class Euler:

    __slots__ = "_v",

    def __init__(self,
                 heading: float = 0.0, pitch: float = 0.0, roll: float = 0.0,
                 _num=is_number):
        assert _num(heading)
        assert _num(pitch)
        assert _num(roll)
        self._v = [heading, pitch, roll]

    def __repr__(self):
        return f"Euler({self._v[0]}, {self._v[1]}, {self._v[2]})"

    @property
    def heading(self):
        return self._v[0]

    @heading.setter
    def heading(self, value):
        self._v[0] = value

    @property
    def pitch(self):
        return self._v[1]

    @pitch.setter
    def pitch(self, value):
        self._v[1] = value

    @property
    def roll(self):
        return self._v[2]

    @roll.setter
    def roll(self, value):
        self._v[2] = value


    def __getitem__(self, index):
        return self._v[index]

    def __setitem__(self, index, value):
        self._v[index] = value

    @property
    def tuple(self):
        return tuple(self._v)

    def __len__(self):
        return 3

    def copy(self):
        return Euler(*self._v)


    def __eq__(self, other):
        return self._v[0] == other[0] and self._v[1] == other[1] and self._v[2] == other[2]

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        for av, bv in zip(self._v, other[:3]):
            if av < bv:
                return True
            elif av > bv:
                return False
        return False

    def equals(self, e, rel = 1e-9, abs = 1e-12,
               _close = math.isclose):
        ''' Compare euler angles with other component-wise using provided tolerances, to ensure euler angles are close to equal''' 
        return _close(self[0], e[0], rel_tol=rel, abs_tol=abs) and \
               _close(self[1], e[1], rel_tol=rel, abs_tol=abs) and \
               _close(self[2], e[2], rel_tol=rel, abs_tol=abs)


    def equiv(self, e, rel = 1e-9, abs = 1e-12):
        ''' Compare euler angles by calculating their quaternions, to ensure that euler angles are equivalent'''
        q1 = euler2quat(self)
        q2 = euler2quat(e)
        return q1.equals(q2, rel, abs) or q1.equiv(q2, rel, abs)


_EUL_INDEX_SAFE = (0, 1, 2, 0)
_EUL_INDEX_NEXT = (1, 2, 0, 1)

def _get_ord(ord, _safe = _EUL_INDEX_SAFE, _next = _EUL_INDEX_NEXT):
    f = ord & 1
    ord >>= 1
    s = ord & 1
    ord >>= 1
    n = ord & 1
    i = _safe[ord & 3]
    j = _next[i + n]
    k = _next[i + 1 - n]
    h = k if s != 0 else i
    return i, j, k, h, n, s, f


def _euler_angles_to_quat(x: float, y: float, z: float, ord: int = 1,
                          _ord = _get_ord,
                          _sin = math.sin,
                          _cos = math.cos):
    ''' heading, pitch, roll (in radians), order == ZYXr '''

    i, j, k, h, n, s, f = _ord(ord)

    if f == 1:
        x, z = z, x

    if n == 1:
        y = -y

    ti = x * 0.5
    tj = y * 0.5
    th = z * 0.5

    ci = _cos(ti)
    cj = _cos(tj)
    ch = _cos(th)

    si = _sin(ti)
    sj = _sin(tj)
    sh = _sin(th)

    cc = ci * ch
    cs = ci * sh
    sc = si * ch
    ss = si * sh

    a = [0, 0, 0]
    if s == 1:
        a[i] = cj * (cs + sc)
        a[j] = sj * (cc + ss)
        a[k] = sj * (cs - sc)
        w = cj * (cc - ss)
    else:
        a[i] = cj * sc - sj * cs
        a[j] = cj * ss + sj * cc
        a[k] = cj * cs - sj * sc
        w = cj * cc + sj * ss
    if n == 1:
        a[j] = -a[j]

    return Quat(a[0], a[1], a[2], w)


class Matrix4x4:

    def __init__(self):
        self.matrix = [[0.0] * 4 for _ in range(4)]

    def __getitem__(self, idx):
        return self.matrix[idx]

    def __setitem__(self, idx, value):
        self.matrix[idx] = value


def _matrix_to_euler_angles(M: Matrix4x4, ord: int = 1,
                            _ord = _get_ord,
                            _atan2 = math.atan2,
                            _eps = 16 * 1.192092896e-07):
    i, j, k, h, n, s, f = _ord(ord)
    if s == 1:
        sy = math.sqrt(M[i][j] * M[i][j] + M[i][k] * M[i][k])
        if sy > _eps:
            x = _atan2(M[i][j], M[i][k])
            y = _atan2(sy, M[i][i])
            z = _atan2(M[j][i], -M[k][i])
        else:
            x = _atan2(-M[j][k], M[j][j])
            y = _atan2(sy, M[i][i])
            z = 0
    else:
        cy = math.sqrt(M[i][i] * M[i][i] + M[j][i] * M[j][i])
        if cy > _eps:
            x = _atan2(M[k][j], M[k][k])
            y = _atan2(-M[k][i], cy)
            z = _atan2(M[j][i], M[i][i])
        else:
            x = _atan2(-M[j][k], M[j][j])
            y = _atan2(-M[k][i], cy)
            z = 0

    if n == 1:
        x = -x
        y = -y
        z = -z

    if f == 1:
        x, z = z, x

    return x, y, z


def _quaternion_to_euler_angles(q: Quat, ord: int = 1,
                                _m2e = _matrix_to_euler_angles,
                                _M = Matrix4x4):
    Nq = q.length2()

    s = 2.0 / Nq if Nq > 0.0 else 0.0

    x, y, z, w = q.x, q.y, q.z, q.w

    xs, ys, zs = x * s, y * s, z * s
    wx, wy, wz = w * xs, w * ys, w * zs
    xx, xy, xz = x * xs, x * ys, x * zs
    yy, yz, zz = y * ys, y * zs, z * zs

    M = _M()
    M[0] = [ 1.0 - yy - zz,           xy - wz,            xz + wy,      0.0]
    M[1] = [       xy + wz,     1.0 - xx - zz,            yz - wx,      0.0]
    M[2] = [       xz - wy,           yz + wx,      1.0 - xx - yy,      0.0]
    M[3] = [           0.0,               0.0,                0.0,      1.0]

    return _m2e(M, ord)


def euler2quat(e: Euler,
               _e2q = _euler_angles_to_quat,
               _rad = math.radians):
    return _e2q(_rad(e.heading), _rad(e.pitch), _rad(e.roll), ord=1)


def quat2euler(q: Quat,
               _q2e = _quaternion_to_euler_angles,
               _deg = math.degrees):
    x, y, z = _q2e(q, ord = 1)
    return Euler(_deg(x), _deg(y), _deg(z))
