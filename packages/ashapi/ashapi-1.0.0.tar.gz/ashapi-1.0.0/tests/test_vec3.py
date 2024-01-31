import pytest

from ashapi import Vec3


def test_vec3_init():

    v = Vec3(42.0, -28, 11)

    assert v[0] == 42.0
    assert v[1] == -28
    assert v[2] == 11

    assert v.x == 42.0
    assert v.y == -28
    assert v.z == 11


@pytest.mark.parametrize("args",
[
    [],
    [0],
    [0, 0],
    [0, 0, 0],
    [1.5, -0.2, 10],
    [42.0],
    [42.0, -28],
    [42.0, -28, 11],
])
def test_vec3_init_args(args):

    v = Vec3(*args)

    x = args[0] if args else 0
    y = args[1] if len(args) > 1 else 0
    z = args[2] if len(args) > 2 else 0

    assert v[0] == x
    assert v[1] == y
    assert v[2] == z

    assert v.x == x
    assert v.y == y
    assert v.z == z


@pytest.mark.parametrize("kwargs",
[
    {},
    {'x': 42.0},
    {'x': 42.0, 'y': -28},
    {'x': 42.0, 'y': -28, 'z': 11},
    {'x': 42.0, 'z': 11},
])
def test_vec3_init_kwargs(kwargs):

    v = Vec3(**kwargs)

    x = kwargs.get('x', 0)
    y = kwargs.get('y', 0)
    z = kwargs.get('z', 0)

    assert v[0] == x
    assert v[1] == y
    assert v[2] == z

    assert v.x == x
    assert v.y == y
    assert v.z == z


def test_vec3_init_wrong():

    with pytest.raises(Exception):
        Vec3("abcd")

    with pytest.raises(Exception):
        Vec3([])

    with pytest.raises(Exception):
        Vec3({})

    with pytest.raises(Exception):
        Vec3([1, 2, 3, 4, 5])

    with pytest.raises(Exception):
        Vec3(None)

    with pytest.raises(Exception):
        Vec3(42.0, None, 11)

    with pytest.raises(Exception):
        Vec3(a=42.0, b=-28, c=11)


def test_vec3_assign():

    v = Vec3()

    v[0] = 5
    v[1] = -7
    v[2] = 15

    assert v[0] == 5
    assert v[1] == -7
    assert v[2] == 15

    v.x = 3
    v.y = -12
    v.z = 3.7

    assert v.x == 3
    assert v.y == -12
    assert v.z == 3.7


def test_vec3_equals():

    v = Vec3(1, 2, 3)
    assert v == v

    a = Vec3()
    b = Vec3()
    assert a == b

    a = Vec3(1, 2, 3)
    b = Vec3(1.0, 2.0, 2.99999)
    assert a != b

    a = Vec3()
    b = [0, 0, 0]
    assert a == b

    a = Vec3()
    b = (0, 0, 0)
    assert a == b

    a = Vec3(1, 2, 3)
    b = [1, 2, 3]
    assert a == b

    a = Vec3(1, 2, 3)
    b = [1.0, 2.0, 2.99999]
    assert a != b


def test_vec3_fields():
    v = Vec3(1, 2, 3)
    assert v[0] == v.x
    assert v[1] == v.y
    assert v[2] == v.z
    v = Vec3(1, 2, 3)
    v[0] += -3
    assert v.x == -2
    assert v == [-2, 2, 3]


def test_vec3_length():
    assert Vec3().length() == 0
    assert Vec3(1, 0, 0).length() == 1
    assert Vec3(0, 1, 0).length() == 1
    assert Vec3(0, 0, 1).length() == 1
    assert Vec3(-1, 0, 0).length() == 1
    assert Vec3(0, -1, 0).length() == 1
    assert Vec3(0, 0, -1).length() == 1
    assert Vec3(1, 2, 3).length() == (1 + 4 + 9) ** 0.5
    assert Vec3(-1, -2, -3).length() == (1 + 4 + 9) ** 0.5
    assert Vec3(1, 2, 3).length2() == 1 + 4 + 9
    assert Vec3(-1, -2, -3).length2() == 1 + 4 + 9


def test_vec3_add():
    a = Vec3(1, 2, 3)
    b = Vec3(4, 5, 6)
    c = a + b
    assert a != c
    assert b != c
    assert a == [1, 2, 3]
    assert b == [4, 5, 6]
    assert c == [5, 7, 9]


def test_vec3_subtract():
    a = Vec3(1, 2, 3)
    b = Vec3(4, 5, 6)
    c = a - b
    d = b - a
    assert a != c
    assert b != c
    assert a == [1, 2, 3]
    assert b == [4, 5, 6]
    assert c == [-3, -3, -3]
    assert d == [3, 3, 3]


def test_vec3_multiply_scalar():
    a = Vec3(1, 2, 3)
    n = 2
    c = a * n
    assert a != c
    assert a == [1, 2, 3]
    assert c == [2, 4, 6]


def test_vec3_divide_scalar():
    a = Vec3(2, 4, 6)
    n = 2
    c = a / n
    assert a != c
    assert a == [2, 4, 6]
    assert c == [1, 2, 3]


def test_vec3_dot():
    a = Vec3(1, 2, 3)
    b = Vec3(4, 5, 6)
    assert a * b == 32

def test_vec3_cross():
    a = Vec3(1, 2, 3)
    b = Vec3(4, 5, 6)
    c = a @ b
    assert a != c
    assert b != c
    assert a == [1, 2, 3]
    assert b == [4, 5, 6]
    assert c == [-3, 6, -3]
    assert c == a ^ b


def test_vec3_normalize():

    v = Vec3(2, 0, 0)
    assert v.normalized == [1, 0, 0]
    assert v == [2, 0, 0]

    v.normalize()
    assert v == [1, 0, 0]

    v = Vec3(0, 2, 0)
    assert v.normalized == [0, 1, 0]
    assert v == [0, 2, 0]

    v.normalize()
    assert v == [0, 1, 0]

    v = Vec3(0, 0, 2)
    assert v.normalized == [0, 0, 1]
    assert v == [0, 0, 2]

    v.normalize()
    assert v == [0, 0, 1]

    v = Vec3(1, 2, 3)
    assert v.normalized == [1 / 14**0.5, 2 / 14**0.5, 3 / 14**0.5]
    assert v == [1, 2, 3]


def test_vec3_negate():
    v = Vec3(1, 2, 3)
    assert -v == [-1, -2, -3]

def test_vec3_copy():
    a = Vec3(1, 2, 3)
    b = a.copy()
    assert a == b
    assert not a._v is b._v
