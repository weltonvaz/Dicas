#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela
fórmula: S = 1 + 1/2 + 1/3 + … + 1/100"""

import os
os.system('clear')

S = 1
for x in range(2,101):
    S = S + (1/x)
print("%.2f" %S)
