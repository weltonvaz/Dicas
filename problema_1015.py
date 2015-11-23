#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
os.system('clear')

from math import sqrt

x1y1 = input()
x2y2 = input()

p1 = x1y1.split()
p2 = x2y2.split()

d1 = (((float(p2[0])) - (float(p1[0])))**2)
d2 = (((float(p2[1])) - (float(p1[1])))**2)

distancia = sqrt(d1+d2)

print("%.4f" %distancia)
