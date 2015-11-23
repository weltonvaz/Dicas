#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""Escrever um programa que leia 2 valores X e Y e que imprima todos os valores
entre eles cujo resto da divisão dele por 5 for igual a 2 ou igual a 3."""

import os
os.system('clear')

X = int(input())
Y = int(input())

if X > Y:
    for z in range(Y+1,X):
        if z % 5 == 2 or z % 5 == 3:
            print(z)
else:
    for z in range(X+1,Y):
        if z % 5 == 2 or z % 5 == 3:
            print(z)
