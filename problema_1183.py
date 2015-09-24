#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Leia um caractere maiúsculo, que indica uma operação que deve ser realizada
e uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média
considerando somente aqueles elementos que estão acima da diagonal principal
da matriz, conforme ilustrado abaixo (área verde).
"""

def soma():
    somam = 0
    matriz = []
    for i in range(0,12):
        for j in range(0,12):
            M = float(input())
            matriz.append(M)
            if j < i:
                somam += M
    return somam

T = input()
if (T == 'S'):
    print("%.1f" %soma())
else:
    media = soma()
    print("%.1f" %(media/6