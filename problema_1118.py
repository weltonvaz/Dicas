#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""Faça um programa que leia as notas referentes às duas avaliações de um
aluno. Calcule e imprima a média semestral. Faça com que o algoritmo só aceite
 notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota
 deve ser validada separadamente."""

import os
os.system('clear')
import sys

def pergunta():
    answer = input("novo calculo (1-sim 2-nao)\n")
    if answer == '1':
        vnotas()
        pergunta()
    elif answer == '2':
        sys.exit()
    else:
        pergunta()

def vnotas():
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

vnotas()
pergunta()
