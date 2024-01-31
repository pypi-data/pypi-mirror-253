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

from . quat import Vec3, Quat


class PQ:

    __slots__ = "p", "q"

    def __init__(self, p: Vec3 = Vec3(), q: Quat = Quat()):
        self.p = p
        self.q = q


def pq_abs(pq: PQ, other: PQ) -> PQ:
    ''' Return absolute transform (PQ) of 'other', when argument 'other' defined relative to 'pq' '''
    return PQ(pq.q * other.p + pq.p, other.q * pq.q)

def pq_absp(pq: PQ, p: Vec3) -> Vec3:
    ''' Return absolute position of p, when p defined relative to 'pq' '''
    return pq.q * p + pq.p

def pq_absv(pq: PQ, v: Vec3,
            _abs = pq_absp) -> Vec3:
    ''' Return absolute vector of v, when v defined relative to 'pq' '''
    return _abs(pq, v) - pq.p

def pq_absq(pq: PQ, q: Quat) -> Quat:
    ''' Return absolute rotation of q, given that argument 'q' defines rotation relative to 'pq' '''
    return q * pq.q

def pq_rel(pq: PQ, other: PQ) -> PQ:
    ''' Return transform (PQ) of 'other' relative to 'pq', when argument 'other' is defined in same (absolute) coordinate frame as 'pq' '''
    q1 = pq.q.inv
    p1 = q1 * pq.p
    return PQ(q1 * other.p - p1, other.q * q1)

def pq_relp(pq: PQ, p: Vec3) -> Vec3:
    ''' Return position relative to 'pq', when argument 'p' defines position in same (absolute) coordinate frame as 'pq' '''
    q1 = pq.q.inv
    p1 = q1 * pq.p
    return q1 * p - p1

def pq_relv(pq: PQ, v: Vec3,
            _rel = pq_relp) -> Vec3:
    ''' Return vector relative to 'pq', when argument 'v' defines vector in same (absolute) coordinate frame as 'pq' '''
    return _rel(pq, v) - _rel(pq, Vec3())


def pq_relq(pq: PQ, q: Quat) -> Quat:
    ''' Return rotation relative to 'pq', when argument 'q' defines rotation in same (absolute) coordinate frame as 'pq' '''
    return q * pq.q.inv


PQ.abs = pq_abs
PQ.absp = pq_absp
PQ.absv = pq_absv
PQ.absq = pq_absq

PQ.rel = pq_rel
PQ.relp = pq_relp
PQ.relv = pq_relv
PQ.relq = pq_relq
