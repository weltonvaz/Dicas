#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula:
S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/?"""

import os
os.system('clear')

soma = 0
j = 1.00

for i in range(1,40,2):
    aux = (i/j)
    soma += aux
    j = j*2

print("%.2f" %soma)
