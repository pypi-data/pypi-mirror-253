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

from . vec3 import Vec3, is_number


class Quat:

    __slots__ = "_v",

    def __init__(self,
                 x: float = 0.0, y: float = 0.0, z: float = 0.0, w: float = 1.0,
                 _num = is_number):
        assert _num(x)
        assert _num(y)
        assert _num(z)
        assert _num(w)
        self._v = [x, y, z, w]

    def __repr__(self):
        return f"Quat({self._v[0]}, {self._v[1]}, {self._v[2]}, {self._v[3]})"


    @property
    def x(self):
        return self._v[0]

    @x.setter
    def x(self, value):
        self._v[0] = value

    @property
    def y(self):
        return self._v[1]

    @y.setter
    def y(self, value):
        self._v[1] = value

    @property
    def z(self):
        return self._v[2]

    @z.setter
    def z(self, value):
        self._v[2] = value

    @property
    def w(self):
        return self._v[3]

    @w.setter
    def w(self, value):
        self._v[3] = value

    def __getitem__(self, index):
        return self._v[index]

    def __setitem__(self, index, value):
        self._v[index] = value

    @property
    def tuple(self):
        return tuple(self._v)

    def copy(self):
        return Quat(*self._v)

    def __bool__(self):
        ''' return False if the Quat represents a zero rotation, and therefore can be ignored in computations '''
        return self != [0, 0, 0, 1]

    def __len__(self):
        return 4

    def __eq__(self, other):
        return self._v[0] == other[0] and self._v[1] == other[1] and self._v[2] == other[2] and self._v[3] == other[3]

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        for av, bv in zip(self._v, other._v):
            if av < bv:
                return True
            elif av > bv:
                return False
        return False

    def equals(self, q, rel = 1e-9, abs = 1e-12,
               _close = math.isclose):
        ''' Compare quat with other component-wise using provided tolerances, to ensure quats are close to equal''' 
        return _close(self[0], q[0], rel_tol=rel, abs_tol=abs) and \
               _close(self[1], q[1], rel_tol=rel, abs_tol=abs) and \
               _close(self[2], q[2], rel_tol=rel, abs_tol=abs) and \
               _close(self[3], q[3], rel_tol=rel, abs_tol=abs)

    def equiv(self, q, rel = 1e-9, abs = 1e-12,
               _close = math.isclose):
        ''' Compare quats by calculating cosine angle between them, to ensure that quats are equivalent''' 
        dot = self[0]*q[0] + self[1]*q[1] + self[2]*q[2] + self[3]*q[3]
        return _close(dot*dot, 1, rel_tol=rel, abs_tol=abs)


    def rotate_vector(self, v: Vec3):
        axis = Vec3(*self._v[:3])
        uv = axis ^ v
        uuv = axis ^ uv
        uv *= 2.0 * self._v[3]
        uuv *= 2.0
        return v + uv + uuv

    # def rotate_vector(self, v: Vec3):
    #     q = self
    #     q_v = Quat(v.x, v.y, v.z, 0) # extend Vec3 to Quat
    #     vv = (q * q_v * q.inv)[:3] # clip the result to list with len 3
    #     return Vec3(*vv)

    def __mul__(self, q_or_v):
        ''' Multiply by another vector or quaternion, q * v, q1 * q2 '''
        size = len(q_or_v)
        if size == 3:
            return self.rotate_vector(q_or_v)
        if size == 4:
            x, y, z, w = self._v
            i, j, k, t = q_or_v
            return Quat( t * x + i * w + j * z - k * y,
                         t * y - i * z + j * w + k * x,
                         t * z + i * y - j * x + k * w,
                         t * w - i * x - j * y - k * z )


    def __imul__(self, q):
        ''' Unary multiply by another quaternion, q1 *= q2 '''
        x, y, z, w = self._v
        i, j, k, t = q
        self._v[0] = t * x + i * w + j * z - k * y
        self._v[1] = t * y - i * z + j * w + k * x
        self._v[2] = t * z + i * y - j * x + k * w
        self._v[3] = t * w - i * x - j * y - k * z
        return self

    def __truediv__(self, q):
        ''' Divide by another quaternion, q1 / q2 '''
        return self * q.inv

    def __itruediv__(self, q):
        ''' Unary divide by another quaternion, q1 /= q2 '''
        self *= q.inv
        return self

    def __neg__(self):
        ''' Negate, returns quaternion with all components negated, which is basically same rotation'''
        return Quat(-self._v[0], -self._v[1], -self._v[2], -self._v[3])

    def __invert__(self):
        ''' Conjugated '''
        return Quat(-self._v[0], -self._v[1], -self._v[2], self._v[3])

    def length2(self, _sum = sum):
        return _sum(a*a for a in self._v)

    def length(self, _sqrt = math.sqrt):
        return _sqrt(self.length2())

    def normalize(self):
        norm = self.length()
        assert norm > 0.0
        self._v[0] /= norm
        self._v[1] /= norm
        self._v[2] /= norm
        self._v[3] /= norm
        return norm

    @property
    def normalized(self):
        norm = self.length()
        assert norm > 0.0
        return Quat(self._v[0] / norm, self._v[1] / norm, self._v[2] / norm, self._v[3] / norm)


    @property
    def conj(self):
        return ~self

    @property
    def inv(self):
        '''Inverse quaternion, e.g. q * q.inv == Quat() '''
        conj = self.conj._v
        norm2 = self.length2()
        return Quat(conj[0] / norm2, conj[1] / norm2, conj[2] / norm2, conj[3] / norm2)

    def make_rotate(self, angle, axis,
                    _eps = 0.0000001,
                    _sqrt = math.sqrt,
                    _sin = math.sin,
                    _cos = math.cos):
        x, y, z = axis
        length = _sqrt(x * x + y * y + z * z)

        if length < _eps:
            self._v = [0.0, 0.0, 0.0, 1.0]
            return

        inversenorm = 1.0 / length
        coshalfangle = _cos(0.5 * angle)
        sinhalfangle = _sin(0.5 * angle)

        self._v[0] = x * sinhalfangle * inversenorm
        self._v[1] = y * sinhalfangle * inversenorm
        self._v[2] = z * sinhalfangle * inversenorm
        self._v[3] = coshalfangle

        return self


    def make_rotate_from_to(self, from_vec, to_vec):
        source_vector = from_vec
        target_vector = to_vec

        from_len2 = source_vector.length2()
        from_len = math.sqrt(from_len2) if (from_len2 < 1.0 - 1e-7) or (from_len2 > 1.0 + 1e-7) else 1.0

        to_len2 = target_vector.length2()
        to_len = math.sqrt(to_len2) if (to_len2 < 1.0 - 1e-7) or (to_len2 > 1.0 + 1e-7) else 1.0

        dot_prod_plus_1 = 1.0 + source_vector * target_vector

        if dot_prod_plus_1 < 1e-7:
            if abs(source_vector.x) < 0.6:
                norm = math.sqrt(1.0 - source_vector.x * source_vector.x)
                self._v = [0.0, source_vector.z / norm, -source_vector.y / norm, 0.0]
            elif abs(source_vector.y) < 0.6:
                norm = math.sqrt(1.0 - source_vector.y * source_vector.y)
                self._v = [-source_vector.z / norm, 0.0, source_vector.x / norm, 0.0]
            else:
                norm = math.sqrt(1.0 - source_vector.z * source_vector.z)
                self._v = [source_vector.y / norm, -source_vector.x / norm, 0.0, 0.0]
        else:
            omega = math.acos(dot_prod_plus_1)
            sinomega = math.sin(omega)
            tmp = source_vector ^ target_vector / (2.0 * sinomega)
            self._v = [tmp.x, tmp.y, tmp.z, math.sqrt(0.5 * dot_prod_plus_1)]


    def slerp(self, t, from_quat, to_quat):
        epsilon = 0.00001
        omega, cosomega, sinomega, scale_from, scale_to = 0.0, 0.0, 0.0, 0.0, 0.0

        cosomega = from_quat.dot(to_quat)
        quat_to = to_quat if cosomega >= 0.0 else -to_quat

        if 1.0 - cosomega > epsilon:
            omega = math.acos(cosomega)
            sinomega = math.sin(omega)
            scale_from = math.sin((1.0 - t) * omega) / sinomega
            scale_to = math.sin(t * omega) / sinomega
        else:
            scale_from = 1.0 - t
            scale_to = t

        self._v = [(from_quat[i] * scale_from + quat_to[i] * scale_to) for i in range(4)]

