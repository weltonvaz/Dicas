#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""Escrever um algoritmo que leia 2 valores inteiros X e Y calcule a soma dos
números que não são múltiplos de 13 entre X e Y, incluindo ambos."""

import os
os.system('clear')

x = int(input())
y = int(input())

soma = 0

if x > y:
    for z in range(y,x+1):
        if z % 13 != 0:
            soma += z
else:
    for z in range(x,y+1):
        if z % 13 != 0:
            soma += z
print(soma)
