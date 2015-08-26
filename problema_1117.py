#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""Faça um programa que leia as notas referentes às duas avaliações de um
aluno. Calcule e imprima a média semestral. Faça com que o algoritmo só aceite
 notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota
 deve ser validada separadamente."""

import os
os.system('clear')

while True:
    x = float(input())
    if x > 10 or x <= 0:
        print("nota invalida")
    else:
        break
while True:
    y = float(input())
    if y > 10 or y <= 0:
        print("nota invalida")
    else:
        break

media = (x+y)/2
print("media = %.2f" %media)
