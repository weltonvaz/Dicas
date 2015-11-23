#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série
de Fibonacci. Nessa sequência, cada número, depois dos 2 primeiros, é igual à
soma dos 2 anteriores. Escreva um algoritmo que leia um inteiro N (N < 46) e
mostre os N primeiros números dessa série."""

import os
os.system('clear')

from math import sqrt

def F(n):
	return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))

num = int(input())

for x in range(0,num):
	if x < (num-1):
		print(F(x),end=" ")
	else:
		print(F(x))
