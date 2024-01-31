import math
import pytest

from ashapi import Vec3, Quat


def test_quat_init():

    q = Quat(0.1, 0.2, 0.3, 1.2)

    assert q[0] == 0.1
    assert q[1] == 0.2
    assert q[2] == 0.3
    assert q[3] == 1.2

    assert q.x == 0.1
    assert q.y == 0.2
    assert q.z == 0.3
    assert q.w == 1.2


@pytest.mark.parametrize("args",
[
    [],
    [0],
    [0, 0],
    [0, 0, 0],
    [0, 0, 0, 1],
    [0.1, 0.2, 0.3, 1],
    [42.0],
    [42.0, -28],
    [42.0, -28, 11],
    [42.0, -28, 11, 10],
])
def test_quat_init_args(args):

    q = Quat(*args)

    x = args[0] if args else 0.0
    y = args[1] if len(args) > 1 else 0.0
    z = args[2] if len(args) > 2 else 0.0
    w = args[3] if len(args) > 3 else 1.0

    assert q[0] == x
    assert q[1] == y
    assert q[2] == z
    assert q[3] == w

    assert q.x == x
    assert q.y == y
    assert q.z == z
    assert q.w == w


@pytest.mark.parametrize("kwargs",
[
    {},
    {'x': 42.0},
    {'x': 42.0, 'y': -28},
    {'x': 42.0, 'y': -28, 'z': 11},
    {'x': 42.0, 'y': -28, 'z': 11, 'w': 2},
    {'x': 42.0, 'z': 11}, 
    {'x': 0}, 
    {'w': 1}, 
    {'w': 10}, 
])
def test_quat_init_kwargs(kwargs):

    v = Quat(**kwargs)

    x = kwargs.get('x', 0)
    y = kwargs.get('y', 0)
    z = kwargs.get('z', 0)
    w = kwargs.get('w', 1)

    assert v[0] == x
    assert v[1] == y
    assert v[2] == z
    assert v[3] == w

    assert v.x == x
    assert v.y == y
    assert v.z == z
    assert v.w == w


def test_quat_init_wrong():

    with pytest.raises(Exception):
        Quat("abcd")

    with pytest.raises(Exception):
        Quat([])

    with pytest.raises(Exception):
        Quat({})

    with pytest.raises(Exception):
        Quat([1, 2, 3, 4, 5])

    with pytest.raises(Exception):
        Quat(None)

    with pytest.raises(Exception):
        Quat(42.0, None, 11)

    with pytest.raises(Exception):
        Quat(a=42.0, b=-28, c=11, d=-5)


def test_quat_assign():

    q = Quat()

    q[0] = 5
    q[1] = -7
    q[2] = 15
    q[3] = 2.5

    assert q[0] == 5
    assert q[1] == -7
    assert q[2] == 15
    assert q[3] == 2.5

    q.x = 3
    q.y = -12
    q.z = 3.7
    q.w = 1.1

    assert q.x == 3
    assert q.y == -12
    assert q.z == 3.7
    assert q.w == 1.1


def test_quat_equals():

    q = Quat(1, 2, 3, 4)
    assert q == q

    a = Quat()
    b = Quat()
    assert a == b
    assert b == a

    a = Quat(1, 2, 3, 4)
    b = Quat(1, 2, 2.99999, 4)
    assert a != b
    assert b != a

    a = Quat()
    b = [0, 0, 0, 1]
    assert a == b
    assert b == a

    a = Quat()
    b = (0, 0, 0, 1)
    assert a == b
    assert b == a

    a = Quat(1, 2, 3, 4)
    b = [1, 2, 3, 4]
    assert a == b
    assert b == a

    a = Quat(1, 2, 3, 4)
    b = [1.0, 2.0, 2.99999, 4]
    assert a != b
    assert b != a


def test_quat_fields():

    q = Quat(1, 2, 3, -4)
    assert q[0] == q.x
    assert q[1] == q.y
    assert q[2] == q.z
    assert q[3] == q.w
    q = Quat(1, 2, 3, -4)
    q[0] += -3
    assert q.x == -2
    assert q == [-2, 2, 3, -4]


def test_quat_length2():

    assert Quat().length2() == 1
    assert Quat(1, 0, 0, 0).length2() == 1
    assert Quat(0, 1, 0, 0).length2() == 1
    assert Quat(0, 0, 1, 0).length2() == 1
    assert Quat(0, 0, 0, 1).length2() == 1
    assert Quat(-1, 0, 0, 0).length2() == 1
    assert Quat(0, -1, 0, 0).length2() == 1
    assert Quat(0, 0, -1, 0).length2() == 1
    assert Quat(0, 0, 0, -1).length2() == 1
    assert Quat(1, 2, 3, 4).length2() == 30
    assert Quat(-1, -2, -3, -4).length2() == 30
    assert Quat(0.5, 0.5, 0, 1).length2() == 1.5
    assert Quat(0, 0, 0, 5).length2() == 25


def test_quat_conj():

    q = Quat(1, 2, 3, 4)
    q_conj = Quat(-1, -2, -3, 4)

    assert q.conj == q_conj
    assert ~q == q_conj
    assert q.length2() == q.conj.length2()
    assert q * q.conj == Quat(w = q.length2())
    assert q.conj * q == Quat(w = q.length2())


def test_quat_inverse():

    q = Quat(0.6, 0, 0, 0.8)
    q_inv = Quat(-0.6, 0, 0, 0.8)

    assert q * q_inv == Quat()
    assert q_inv * q == Quat()
    assert q * q.inv == q.inv * q

    # NB: take care about floating point inaccuracy
    assert q.inv == q_inv
    assert q.inv * q == Quat()
    assert q * q.inv == Quat()


def test_quat_make_rotate():

    # Orts
    i = Vec3(1, 0, 0)
    j = Vec3(0, 1, 0)
    k = Vec3(0, 0, 1)

    # Unit quat - no rotation
    qn = Quat(0, 0, 0, 1)

    qr = Quat().make_rotate(0, i)

    assert qr.equals(qn) or qr.equiv(qn)

    # Rotation around x by 90 degrees
    qn = Quat(1, 0, 0, 1).normalized
    qr = Quat().make_rotate(math.radians(90), i)

    assert qr.equals(qn) or qr.equiv(qn)

    # Rotation around y by 90 degrees
    qn = Quat(0, 1, 0, 1).normalized
    qr = Quat().make_rotate(math.radians(90), j)

    assert qr.equals(qn) or qr.equiv(qn)

    # Rotation around z by 90 degrees
    qn = Quat(0, 0, 1, 1).normalized
    qr = Quat().make_rotate(math.radians(90), k)

    assert qr.equals(qn) or qr.equiv(qn)

    # Rotation around x by 180 degrees
    qn = Quat(1, 0, 0, 0)
    qr = Quat().make_rotate(math.radians(180), i)

    assert qr.equals(qn) or qr.equiv(qn)

    # Rotation around y by 180 degrees
    qn = Quat(0, 1, 0, 0)
    qr = Quat().make_rotate(math.radians(180), j)

    assert qr.equals(qn) or qr.equiv(qn)

    # Rotation around z by 180 degrees
    qn = Quat(0, 0, 1, 0)
    qr = Quat().make_rotate(math.radians(180), k)

    assert qr.equals(qn) or qr.equiv(qn)

    # negative tests

    # Rotation around z by 180 degrees versus Rotation around x by 180 degrees
    qn = Quat(0, 0, 1, 0)
    qr = Quat().make_rotate(math.radians(180), i)

    assert not qr.equals(qn) or not qr.equiv(qn)

    # Rotation around y by 180 degrees versus Rotation around x by 90 degrees
    qn = Quat(0, 1, 0, 0)
    qr = Quat().make_rotate(math.radians(90), i)

    assert not qr.equals(qn) or not qr.equiv(qn)


def test_quat_multiply_vector():
    
    # Orts
    i = Vec3(1, 0, 0)
    j = Vec3(0, 1, 0)
    k = Vec3(0, 0, 1)

    # Arbitrary vector
    v = Vec3(1, 2, 3)

    # Unit quat - no rotation
    q = Quat(0, 0, 0, 1)

    assert q * i == i
    assert q * j == j
    assert q * k == k
    assert q * v == v

    # Rotation around x by 90 degrees
    q = Quat(1, 0, 0, 1).normalized

    assert (q * i).equals(i)
    assert (q * j).equals(k)
    assert (q * k).equals(-j)
    assert (q * v).equals( Vec3(1, -3, 2) )

    # Rotation around y by 90 degrees
    q = Quat(0, 1, 0, 1).normalized

    assert (q * i).equals(-k)
    assert (q * j).equals(j)
    assert (q * k).equals(i)
    assert (q * v).equals( Vec3(3, 2, -1) )

    # Rotation around z by 90 degrees
    q = Quat(0, 0, 1, 1).normalized

    assert (q * i).equals(j)
    assert (q * j).equals(-i)
    assert (q * k).equals(k)
    assert (q * v).equals( Vec3(-2, 1, 3) )

    # Rotation around x by 180 degrees
    q = Quat(1, 0, 0, 0)

    assert q * i == i
    assert q * j == -j
    assert q * k == -k
    assert (q * v).equals( Vec3(1, -2, -3) )

    # Rotation around y by 180 degrees
    q = Quat(0, 1, 0, 0)

    assert q * i == -i
    assert q * j == j
    assert q * k == -k
    assert (q * v).equals( Vec3(-1, 2, -3) )

    # Rotation around z by 180 degrees
    q = Quat(0, 0, 1, 0)

    assert q * i == -i
    assert q * j == -j
    assert q * k == k
    assert (q * v).equals( Vec3(-1, -2, 3) )

    # Rotation than inverse rotation
    q = Quat(1, 2, 3, 4).normalized
    v = Vec3(5, -3, 2)
    assert (q.inv * (q * v)).equals( v )


def test_quat_multiply():
    
    q1 = Quat(1, 0, 0, 3)
    q2 = Quat(5, 1, -2, 0)
    q21 = Quat(15, 5, -5, -5)
    q12 = Quat(15, 1, -7, -5)

    assert q12.equals(q1 * q2)
    assert q21.equals(q2 * q1)

    q1 = Quat(1, 2, 3, 4)
    q2 = Quat(5, -1, -3, 7)
    q21 = Quat(24, 28, -2, 34)
    q12 = Quat(30, -8, 20, 34)

    assert q12.equals(q1 * q2)
    assert q21.equals(q2 * q1)


def test_quat_divide():
    
    q1 = Quat(0.6, 0, 0, 0.8)
    q2 = Quat(0, -0.8, 0, 0.6)
    q21 = Quat(0.36, -0.64, -0.48, 0.48)
    q12 = Quat(0.36, -0.64, 0.48, 0.48)

    assert q1.equals(q12 / q2)
    assert q2.equals(q21 / q1)

def test_quat_copy():

    q1 = Quat(1, 2, 3, 4)
    q2 = q1

    assert q2 == q1
    assert q2 is q1

    q3 = q1.copy()

    assert q3 == q1
    assert not (q3 is q1)
