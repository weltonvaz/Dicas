#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Leia um valor inteiro N. Este valor será a quantidade de valores inteiros X
que serão lidos em seguida. Mostre quantos destes valores X estão dentro do
intervalo [10,20] e quantos estão fora do intervalo, mostrando essas informações."""

import os
os.system('clear')

N = int(input())

inn = 0
out = 0

for z in range(1,N+1):
    X = int(input())
    if X >= 10 and X <= 20:
        inn += 1
    else:
        out += 1


print("%d in" %inn)
print("%d out" %out)
