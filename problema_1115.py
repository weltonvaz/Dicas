#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Escreva um programa para ler as coordenadas (X,Y) de uma quantidade
indeterminada de pontos no sistema cartesiano. Para cada ponto escrever o
quadrante a que ele pertence. O algoritmo será encerrado quando pelo menos uma
de duas coordenadas for NULA (nesta situação sem escrever mensagem alguma)."""

import os
os.system('clear')


while True:
    punkt = input()

    X,Y = punkt.split()

    x = float(X)
    y = float(Y)

    if (x == 0):
    	break
    elif (y == 0):
    	break
    elif (x > 0 and y > 0):
    	print("primeiro")
    elif (x < 0 and y > 0):
    	print("segundo")
    elif (x < 0 and y < 0):
    	print("terceiro")
    else:
    	print("quarto")
