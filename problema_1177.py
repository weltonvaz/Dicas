
# -*- coding: utf-8 -*-

"""Faça um programa que leia um valor T e preencha um vetor N[1000] com a
sequência de valores de 0 até T-1 repetidas vezes, conforme exemplo abaixo.
Imprima o vetor N."""

import os
os.system('clear')

N = [0]
n = 0

t = int(input())
while t < 2 or t >= 51:
    t = int(input())

for i in range(1,1000):
    if n >= (t-1):
        n = 0
        N.append(n)
    else:
        n += 1
        N.append(n)

for z in range(0,1000):
    print("N[%d] = %d" %(z,N[z]))
