#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Neste problema você deve ler um número que indica uma coluna de uma matriz na
qual uma operação deve ser realizada, um caractere maiúsculo, indicando a
operação que será realizada, e todos os elementos de uma matriz M[12][12].
Em seguida, calcule e mostre a soma ou a média dos elementos que estão na área
verde da matriz, conforme for o caso. A imagem abaixo ilustra o caso da entrada
do valor 5 para a coluna da matriz, demonstrando os elementos que deverão ser
considerados na operação."""

import os
os.system('clear')

def soma():
	somam = 0
	matriz = []
	for i in range(0,12):
		for j in range(0,12):
			M = float(input())
			matriz.append(M)
			if j < i:
				somam += M
	return somam

T = input()
if (T == 'S'):
	print("%.1f" %soma())
else:
	media = soma()
	print("%.1f" %(media/66.0))
