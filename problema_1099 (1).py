#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Leia um valor inteiro N que é a quantidade de casos de teste que vem a
seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar
 a soma de todos os ímpares existentes entre X e Y."""

import os
os.system('clear')

def drange(start, stop, step):
     r = start
     while r < stop:
     	yield r
     	r += step

i0=drange(0.0, 1.0, 0.1)
["%g" % x for x in i0]