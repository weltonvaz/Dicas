#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Leia um valor inteiro N que é a quantidade de casos de teste que vem a
seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar
 a soma de todos os ímpares existentes entre X e Y."""

import os
os.system('clear')

def simpares(x,y):
    impares = 0
    if x > y:
        for z in range(y+1,x):
            if z % 2 != 0:
                impares = impares + z
    else:
        for z in range(x+1,y):
            if z % 2 != 0:
                impares += z
    return impares

N = int(input())

for z in range(0,N):
    wert = input()
    X,Y = wert.split()
    print(simpares(int(X),int(Y)))
