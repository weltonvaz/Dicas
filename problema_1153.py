#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""Ler um valor N. Calcular e escrever seu respectivo fatorial. Fatorial de
N = N * (N-1) * (N-2) * (N-3) * ... * 1."""

import os
os.system('clear')

n = int(input())

ergebnis = 1
lista = range(1,n+1)

for x in lista:
    ergebnis = x * ergebnis

print(ergebnis)
