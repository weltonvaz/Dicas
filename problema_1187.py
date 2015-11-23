#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e
uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média
considerando somente aqueles elementos que estão acima da diagonal secundária da
matriz, conforme ilustrado abaixo (área verde)."""

import os
os.system('clear')

def soma():
    somam = 0
    matriz = []
    for i in range(0,12):
        for j in range(0,12):
            M = float(input())
            matriz.append(M)
            if (j > i and (j+i) < 11):
                somam += M
    return somam

T = input()
if (T == 'S'):
    print("%.1f" %soma())
else:
    media = soma()
    print("%.1f" %(media/66.0))
