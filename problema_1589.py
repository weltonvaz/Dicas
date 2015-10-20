#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Qual o menor raio do conduite que você deve comprar? Em outras palavras,dado
dois círculos, qual o raio do menor círculo que possa englobar ambos os dois?"""

import os
os.system("clear")

T = int(input())

while T >= 1:
    wert = input()
    R1,R2 = wert.split()
    r1 = int(R1)
    r2 = int(R2)
    raio = r1 + r2
    print(raio)
    T -= 1
