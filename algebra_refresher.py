# -*- coding: utf-8 -*-
"""
Spyder Editor
.
This is a temporary script file.
"""

from math import sqrt, pi, degrees, acos
import numpy as np

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')
            
    def suma(self, v):
        res = [round(x + y, 3) for x, y in zip(self.coordinates, v.coordinates)]
        return(res)
    
    def subt(self, v):
        res = [round(x - y, 3) for x, y in zip(self.coordinates, v.coordinates)]
        return(res)
    
    def mult(self, v):
        res = [round(x * v, 3) for x in self.coordinates]
        return(res)
    
    def magn(self):
        seq = range(len(self.coordinates))
        res = 0
        for x in seq:
            res += self.coordinates[x]**2
        fin = round(sqrt(res), 3)
        return(fin)
    
    def normalize(self):
        try:
            norm_magn = self.magn()
            return(self.mult(1 / norm_magn))
        except ZeroDivisionError:
            raise Exception('Cannot normalize by zero!')
            
    def dot_prod(self, v):
        res = 0
        for x, y in zip(self.coordinates, v.coordinates):
            res += x * y
        return(round(res, 3))
        
    def angle_with(self, v, in_degrees=False):
        u1 = self.normalize()
        u2 = v.normalize()
        angle_in_radians = acos(u1.dot_prod(u2))
        
        if in_degrees:
            degrees_radian = 180. / pi
            return(angle_in_radians / degrees_radian)
        else:
            return angle_in_radians

    def __str__(self):
        return('Vector: {}'.format(self.coordinates))


    def __eq__(self, v):
        return(self.coordinates == v.coordinates)

hey = Vector([8.218, -9.341])
ho = Vector([-1.129, 2.111])

# addition and subtraction
hey.suma(ho)
hey.subt(ho)

# Multiplication
new = Vector([1.671, -1.012, -0.318])
new.mult(7.41)

# Magnitude
Vector([-0.221, 7.437]).magn()
Vector([8.813, -1.331, -6.247]).magn()

 # Normalization   
Vector([5.581, -2.136]).normalize()
Vector([1.996, 3.108, -4.554]).normalize()

# Dot product
v = Vector([7.887, 4.138])
w = Vector([-8.802, 6.776])
v.dot_prod(w)

v = Vector([-5.955, -4.904, -1.874])
w = Vector([-4.496, -8.755, 7.103])
v.dot_prod(w)

# Radians
v = Vector([1, 2, -1])
w = Vector([3, 1, 0])


v.dot_prod(w) / v.magn() * w.magn()