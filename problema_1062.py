#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Leia 6 valores. Em seguida, mostre quantos destes valores digitados foram
positivos. Na próxima linha, deve-se mostrar a média de todos os valores
positivos digitados, com um dígito após o ponto decimal."""

import os
os.system('clear')

positivo = 0
media = 0

for x in range (1,7):
    x = input()
    if float(x) > 0:
        positivo += 1
        media = float(x) + media
print ("%d valores positivos" %positivo)
print ("%.1f" %(float(media)/float(positivo)))
