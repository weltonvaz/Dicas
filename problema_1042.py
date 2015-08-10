#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Leia 3 valores inteiros e ordene-os em ordem crescente. No final,
mostre os valores em ordem crescente, uma linha em branco e em seguida,
os valores na sequência como foram lidos.'''

import os
os.system('clear')

wert = input()

A,B,C = wert.split()

a = int(A)
b = int(B)
c = int(C)
x = [a,b,c]
y = list(x)
y.sort()

for z in y:
	print(z)
print()
for w in x:
	print(w)

"""for w in len(y)+1:
	print(y[w])
for z in x:
	print(z)"""
