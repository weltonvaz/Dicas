
# -*- coding: utf-8 -*-

"""Faça um programa que leia um vetor X[10]. Substitua a seguir, todos os
valores nulos e negativos do vetor X por 1. Em seguida mostre o vetor X."""

import os
os.system('clear')

X = []
wert = int(input())
X.append(wert)
print("N[0] = %d" %(wert))
for i in range(1,10):
    wert = wert * 2
    print("N[%d] = %d" %(i,wert))
    X.append(wert)
