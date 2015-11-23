#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""Ler um número inteiro N e calcular todos os seus divisores."""

import os
os.system('clear')

anzahl = int(input())
zirkel = []

for x in range(1,(anzahl+1)):
    zir = divmod(anzahl,x)
    if zir[1] == 0:
        print(x)
