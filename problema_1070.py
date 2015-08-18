#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Leia um valor inteiro X. Em seguida apresente os 6 valores ímpares
consecutivos a partir de X, um valor por linha, inclusive o X ser for o caso."""

import os
os.system('clear')
 
X = int(input())
 
if X % 2 == 0:
    X += 1
    for Y in range(0,11,2):
        Z = X + Y
        print (Z)
else:
    for Y in range(0,11,2):
        Z = X + Y
        print (Z)