#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""Leia um valor inteiro N que é a quantidade de casos de teste que vem a
seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve
apresentar a soma de Y ímpares consecutivos a partir de X inclusive o próprio X
se ele for ímpar. Por exemplo: para a entrada 4 5, a saída deve ser 45, que é
equivalente à: 5 + 7 + 9 + 11 + 13 para a entrada 7 4, a saída deve ser 40, que
é equivalente à: 7 + 9 + 11 + 13"""

import os
os.system('clear')

def sungerade(x,y):
    soma = 0
    if x % 2 == 0:
        x = x + 1
    for z in range(x,(x+(y*2))):
        if z % 2 != 0:
            soma = soma + z
    return soma

wert = int(input())
for x in range(0,wert):
    X,Y = input().split()
    print(sungerade(int(X),int(Y)))
