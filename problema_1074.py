#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Leia um valor inteiro N. Apresente o quadrado de cada um dos valores pares,
de 1 até N, inclusive N, se for o caso."""

import os
os.system('clear')

N = int(input())
contador = 1

while contador <= N:
    X = int(input())
    if X % 2 == 0 and X > 0:
        print ("EVEN POSITIVE")
    elif X % 2 == 0 and X < 0:
        print ("EVEN NEGATIVE")
    elif X % 2 != 0 and X > 0:
        print ("ODD POSITIVE")
    elif X % 2 != 0 and X < 0:
        print ("ODD NEGATIVE")
    else:
        print ("NULL")
    contador += 1
