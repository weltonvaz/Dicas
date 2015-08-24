#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Escreva um algoritmo que leia 2 números e imprima o resultado da divisão do
primeiro pelo segundo. Caso não for possível mostre a mensagem “divisao
impossivel” para os valores em questão."""

import os
os.system('clear')

N = int(input())
for a in range(0,N):
    wert = int(input())
    X,Y = wert.split()
    x = int(X)
    y = int(Y)
    if y == 0:
        print("divisao impossivel")
    else:
        divisao = X / Y
        print("%.1f" %divisao)
