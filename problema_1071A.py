#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números
impares entre eles."""

import os
os.system('clear')

X = int(input())
Y = int(input())

if X > Y:
    nums = range(Y,X)
else:
    nums = range(X,Y)

impares = list(filter(lambda x: x % 2,nums))

if impares[0] == X or impares[0] == Y:
    del impares[0]
if impares[-1] == X or impares[-1] == Y:
    del impares[-1]

print(sum(impares))
