
# -*- coding: utf-8 -*-

"""Faça um programa que leia um vetor X[10]. Substitua a seguir, todos os
valores nulos e negativos do vetor X por 1. Em seguida mostre o vetor X."""

import os
os.system('clear')

X = []

for i in range(0,10):
    wert = int(input())
    if wert <= 0:
        wert = 1
        X.append(wert)
    else:
        X.append(wert)
    print("X[%d] = %d" %(i,wert))
