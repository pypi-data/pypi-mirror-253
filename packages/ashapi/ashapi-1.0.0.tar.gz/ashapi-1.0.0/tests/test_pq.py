import math
import pytest

from ashapi import Vec3, Quat, PQ, Euler, euler2quat


@pytest.mark.parametrize("position, rotation, body_position",  [
    ( Vec3(5,6,7), Euler(35,45,-10),  Vec3(5,7,-9) ),
    ( Vec3(-5,16,-3.2), Euler(3.2,0,-11),  Vec3(2.2,0,1.3) ),
    ( Vec3(0,0,0), Euler(0,0,-10),  Vec3(1,0,0) ),
])
def test_pq_v(position, rotation, body_position):

    # Position and orientation of local basis in global
    pq = PQ( position, euler2quat( rotation ))

    # Orts
    i = Vec3(1,0,0)
    j = Vec3(0,1,0)
    k = Vec3(0,0,1)

    # New (local) basis (a,b,c) in old (global) basis (i,j,k)
    a = pq.q * i
    b = pq.q * j
    c = pq.q * k

    assert a.equals(pq.absv(i))
    assert b.equals(pq.absv(j))
    assert c.equals(pq.absv(k))

    # Transformation matrix
    a11,a12,a13 = a.x,b.x,c.x
    a21,a22,a23 = a.y,b.y,c.y
    a31,a32,a33 = a.z,b.z,c.z

    # Transformation matrix determinant
    det = a11 * (a22 * a33 - a32 * a23) - a12 * (a21 * a33 - a23 * a31) + a13 * (a21 * a32 - a22 * a31)

    assert math.isclose( det, 1 )

    # Some vector in local coordinates
    v = body_position

    # Same vector in global coordinates (transformed by PQ function)
    u = pq.absv(v)

    # Check using transformation matrix
    assert math.isclose( a11 * v.x + a12 * v.y + a13 * v.z, u.x )
    assert math.isclose( a21 * v.x + a22 * v.y + a23 * v.z, u.y )
    assert math.isclose( a31 * v.x + a32 * v.y + a33 * v.z, u.z )


    # Check direct then inverse transformations
    assert pq.absv(pq.relv(v)).equals(v)
    assert pq.relv(pq.absv(v)).equals(v)

    # check absp
    assert pq.absp(v) == pq.absv(v) + pq.p


@pytest.mark.parametrize("position, rotation, body_orientation",  [
    ( Vec3(5,6,7),  Quat(1,2,3,4).normalized,  Quat(3,5,-1,4).normalized ),
    ( Vec3(0,0,0),  Quat(0,0,3,4).normalized,  Quat(1,2,3,4).normalized ),
    ( Vec3(-5,6,7), Quat(1,-2,0,4).normalized,  Quat(0,1,0,1).normalized ),
    ( Vec3(5,6,7), Quat(0,0,0,1).normalized,  Quat(3,5,-1,4).normalized ),
    ( Vec3(5,0,0),  Quat(3,5,-1,4).normalized,  Quat(0,0,0,1).normalized ),
])
def test_pq_q(position, rotation, body_orientation):

    # Position and orientation of local coordinate system in global coordinate system
    pq = PQ( position, rotation )

    # Orts
    i = Vec3(1,0,0)
    j = Vec3(0,1,0)
    k = Vec3(0,0,1)

    # Some rotation operator given in local system as a quat
    q_local = body_orientation

    # Orts transformed by q_local
    ii = q_local * i
    jj = q_local * j
    kk = q_local * k

    # q_local operator matrix
    B11,B12,B13 = ii.x,jj.x,kk.x
    B21,B22,B23 = ii.y,jj.y,kk.y
    B31,B32,B33 = ii.z,jj.z,kk.z
    
    # Calculate q_global using absq
    q_global = pq.absq(q_local)

    # Orts transformed by q_global
    ii = q_global * i
    jj = q_global * j
    kk = q_global * k

    # q_global operator matrix
    A11,A12,A13 = ii.x,jj.x,kk.x
    A21,A22,A23 = ii.y,jj.y,kk.y
    A31,A32,A33 = ii.z,jj.z,kk.z

    # Orts transformed by basis transformation pq
    ii = pq.q * i
    jj = pq.q * j
    kk = pq.q * k

    # Basis transformation matrix
    T11,T12,T13 = ii.x,jj.x,kk.x
    T21,T22,T23 = ii.y,jj.y,kk.y
    T31,T32,T33 = ii.z,jj.z,kk.z

    # assert A = T*B
    assert math.isclose(A11, T11 * B11 + T12 * B21 + T13 * B31)
    assert math.isclose(A12, T11 * B12 + T12 * B22 + T13 * B32)
    assert math.isclose(A13, T11 * B13 + T12 * B23 + T13 * B33)
    assert math.isclose(A21, T21 * B11 + T22 * B21 + T23 * B31)
    assert math.isclose(A22, T21 * B12 + T22 * B22 + T23 * B32)
    assert math.isclose(A23, T21 * B13 + T22 * B23 + T23 * B33)
    assert math.isclose(A31, T31 * B11 + T32 * B21 + T33 * B31)
    assert math.isclose(A32, T31 * B12 + T32 * B22 + T33 * B32)
    assert math.isclose(A33, T31 * B13 + T32 * B23 + T33 * B33)


    # Check direct then inverse transformations
    assert pq.absq(pq.relq(q_local)).equals(q_local)
    assert pq.relq(pq.absq(q_local)).equals(q_local)


@pytest.mark.parametrize("position, rotation, body_position, body_orientation",  [
    ( Vec3(5,6,7),  Quat(1,2,3,4).normalized, Vec3(0.5,6,7), Quat(3,5,-1,4).normalized ),
    ( Vec3(0,0,0),  Quat(0,0,3,4).normalized, Vec3(-5,6,7), Quat(1,2,3,4).normalized ),
    ( Vec3(-5,6,7), Quat(1,-2,0,4).normalized, Vec3(5.2,6,7), Quat(0,1,0,1).normalized ),
    ( Vec3(5,6,7), Quat(0,0,0,1).normalized, Vec3(0,0,0), Quat(3,5,-1,4).normalized ),
    ( Vec3(5,0,0),  Quat(3,5,-1,4).normalized, Vec3(-1,0,0), Quat(0,0,0,1).normalized ),
])
def test_pq(position, rotation, body_position, body_orientation):

    pq = PQ( position, rotation )
    v = body_position
    q = body_orientation

    assert pq.abs(PQ(v,q)).p == pq.absp(v)
    assert pq.abs(PQ(v,q)).q == pq.absq(q)


    # Check direct then inverse transformations
    assert pq.abs(pq.rel(PQ(v,q))).p.equals(v)
    assert pq.abs(pq.rel(PQ(v,q))).q.equals(q)
    assert pq.rel(pq.abs(PQ(v,q))).p.equals(v)
    assert pq.rel(pq.abs(PQ(v,q))).q.equals(q)