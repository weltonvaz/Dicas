#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Leia 1 valor inteiro N, que representa o número de casos de teste que vem a
seguir. Cada caso de teste consiste de 3 valores reais, cada um deles com uma
casa decimal. Apresente a média ponderada para cada um destes conjuntos de 3
valores, sendo que o primeiro valor tem peso 2, o segundo valor tem peso 3 e o
terceiro valor tem peso 5."""

import os
os.system('clear')

N = int(input())
count = 3

for x in range(0,N):
    media = input()
    p1,p2,p3 = media.split()
    media = (float(p1)*2 + float(p2)*3 + float(p3)*5)/(2+3+5)
    print("%.1f" %media)
    
