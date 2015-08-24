#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Leia uma quantidade indeterminada de duplas de valores inteiros X e Y.
Escreva para cada X e Y uma mensagem que indique se estes valores foram
digitados em ordem crescente ou decrescente."""

import os
os.system('clear')


while True:
    wert = input()
    M,N = wert.split()
    x = int(M)
    y = int(N)
    if x == y:
        break
    else:
        if x > y:
            print("Decrescente")
        else:
            print("Crescente")
