#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram
pares, quantos valores digitados foram ímpares, quantos valores digitados foram
positivos e quantos valores digitados foram negativos."""

import os
os.system('clear')

pares = 0
impares = 0
positivos = 0
negativos = 0


for x in range(0,5):
    x = int(input())
    if x % 2 == 0:
        pares += 1
    if x > 0 and x != 0:
        positivos += 1
    elif x < 0 and x != 0:
        negativos += 1

impares = (5 - pares)

print ("%d valor(es) par(es)" %pares)
print ("%d valor(es) impar(es)" % impares)
print ("%d valor(es) positivo(s)" %positivos)
print ("%d valor(es) negativo(s)" %negativos)
