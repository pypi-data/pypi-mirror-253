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

def is_number(x, _int=int, _float=float, _type=type):
    return _type(x) == _float or _type(x) == _int


class Vec3:

    __slots__ = "_v",

    def __init__(self,
                 x: float = 0.0, y: float = 0.0, z: float = 0.0,
                 _num=is_number):
        assert _num(x)
        assert _num(y)
        assert _num(z)
        self._v = [x, y, z]

    def __repr__(self):
        return f"Vec3({self._v[0]}, {self._v[1]}, {self._v[2]})"

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
    def len(self):
        return self.length()

    @property
    def len2(self):
        return self.length2()

    @property
    def tuple(self):
        return tuple(self._v)

    @property
    def normalized(self):
        n = self.length()
        return Vec3() if n == 0 else self / n

    def __getitem__(self, index):
        return self._v[index]

    def __setitem__(self, index, value):
        self._v[index] = value

    def __len__(self):
        return 3

    def length(self, _sqrt = math.sqrt):
        return _sqrt(self.length2())

    def length2(self, _sum = sum):
        return _sum(a*a for a in self._v)

    def normalize(self):
        norm = self.length()
        if norm > 0.0:
            self._v[0] /= norm
            self._v[1] /= norm
            self._v[2] /= norm
        return norm


    def copy(self):
        return Vec3(*self._v)


    def __eq__(self, other):
        return self._v[0] == other[0] and self._v[1] == other[1] and self._v[2] == other[2]

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        return self.length2() < Vec3(*other).length2()


    def equals(self, v, rel = 1e-9, abs = 1e-12,
               _close = math.isclose):
        ''' Compare vector with other component-wise using provided tolerances, to ensure vectors are close to equal''' 
        return _close(self[0], v[0], rel_tol=rel, abs_tol=abs) and \
               _close(self[1], v[1], rel_tol=rel, abs_tol=abs) and \
               _close(self[2], v[2], rel_tol=rel, abs_tol=abs)


    def __neg__(self):
        ''' Negation, -a '''
        return Vec3(-self._v[0], -self._v[1], -self._v[2])

    def __add__(self, other):
        ''' Vectors add, a += b '''
        return Vec3(self._v[0] + other[0], self._v[1] + other[1], self._v[2] + other[2])

    def __iadd__(self, other):
        ''' Unary vectors add, a += b '''
        self._v[0] += other[0]
        self._v[1] += other[1]
        self._v[2] += other[2]
        return self

    def __sub__(self, other):
        ''' Vectors substract, a - b '''
        return Vec3(self._v[0] - other[0], self._v[1] - other[1], self._v[2] - other[2])

    def __isub__(self, other):
        ''' Unary vectors substract, a -= b '''
        self._v[0] -= other[0]
        self._v[1] -= other[1]
        self._v[2] -= other[2]
        return self

    def __mul__(self, other):
        ''' Multiply by scalar or vector dot product, a * n (or a * b)'''
        if is_number(other):
            return Vec3(self._v[0] * other, self._v[1] * other, self._v[2] * other)
        return  self._v[0] * other[0] + self._v[1] * other[1] + self._v[2] * other[2]

    def __imul__(self, scalar):
        ''' Unary multiply by scalar, a *= n '''
        self._v[0] *= scalar
        self._v[1] *= scalar
        self._v[2] *= scalar
        return self

    def __truediv__(self, scalar):
        ''' Divide by scalar, a / n'''
        return Vec3(self._v[0] / scalar, self._v[1] / scalar, self._v[2] / scalar)

    def __itruediv__(self, scalar):
        ''' Unary divide by scalar, a /= n '''
        self._v[0] /= scalar
        self._v[1] /= scalar
        self._v[2] /= scalar
        return self

    def __matmul__(self, other):
        ''' Cross product, a @ b '''
        return Vec3(
            self._v[1] * other[2] - self._v[2] * other[1],
            self._v[2] * other[0] - self._v[0] * other[2],
            self._v[0] * other[1] - self._v[1] * other[0]
        )

    def __xor__(self, other):
        ''' Cross product, a ^ b '''
        return self @ other

    def __pow__(self, other):
        ''' Multiply by vector components, a ** b '''
        return Vec3(self._v[0] * other[0], self._v[1] * other[1], self._v[2] * other[2])

    def __floordiv__(self, other):
        ''' Divide by vector components, a // b '''
        return Vec3(self._v[0] / other[0], self._v[1] / other[1], self._v[2] / other[2])

