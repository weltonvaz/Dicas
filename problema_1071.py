#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números
impares entre eles."""

import os
os.system('clear')

X = int(input())
Y = int(input())

ungerade = []
if X > Y:
    for z in range(Y,X):
        if z % 2 != 0:
            ungerade.append(z)
    if ungerade[0] == X or ungerade[0] == Y:
        del ungerade[0]
    if ungerade[-1] == X or ungerade[-1] == Y:
        del ungerade[-1]

else:
    for z in range(X,Y):
        if z % 2 != 0:
            ungerade.append(z)
    if ungerade[0] == X or ungerade[0] == Y:
        del ungerade[0]
    if ungerade[-1] == X or ungerade[-1] == Y:
        del ungerade[-1]

print(len(ungerade))
print(ungerade)
