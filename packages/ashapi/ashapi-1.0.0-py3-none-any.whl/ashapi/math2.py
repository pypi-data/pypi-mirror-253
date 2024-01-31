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

import sys
import math

isclose = math.isclose


deg2rad = math.radians
rad2deg = math.degrees


METERS_PER_SECOND_TO_KNOT = 3600 / 1852
KNOT_TO_METERS_PER_SECOND = 1852 / 3600


def knots2msec(k, _ratio = KNOT_TO_METERS_PER_SECOND):
    return k * _ratio


def msec2knots(v, _ratio = METERS_PER_SECOND_TO_KNOT):
    return v * _ratio


def clamp(value, lower, upper):
    return lower if value < lower else upper if value > upper else value


def shortest_arc(from_deg: float, to_deg: float,
                 _abs = abs):
    ''' Return shortest distance on circle (always positive) between two angles'''
    diff = _abs(to_deg - from_deg) % 360
    return 180 - _abs(diff - 180)
    # diff = ( to_deg - from_deg ) % 360
    # if diff > 180 :
    #     diff = -(360 - diff)
    # return diff


def aabb2d(points, 
           x_max=-sys.float_info.max,
           y_max=-sys.float_info.max,
           x_min=sys.float_info.max,
           y_min=sys.float_info.max,
           _max=max,
           _min=min):
  xx = [p[0] for p in points]
  yy = [p[1] for p in points]
  x_max = _max(x_max, _max(xx))
  y_max = _max(y_max, _max(yy))
  x_min = _min(x_min, _min(xx))
  y_min = _min(y_min, _min(yy))
  return (x_max, y_max, x_min, y_min)
