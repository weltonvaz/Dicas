
# -*- coding: utf-8 -*-

"""Faça um programa que leia um valor T e preencha um vetor N[1000] com a
sequência de valores de 0 até T-1 repetidas vezes, conforme exemplo abaixo.
Imprima o vetor N."""

import os
os.system('clear')

X = float(input())
N = [X]

print("N[0] = %.4f" %(X))
for x in range(1,100):
    X = X / 2
    N.append(X)
    print("N[%d] = %.4f" %(x,X))
