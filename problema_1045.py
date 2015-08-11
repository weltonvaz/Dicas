#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem
decrescente, de modo que o lado A representa o maior dos 3 lados.
A seguir, determine o tipo de triângulo que estes três lados formam, com
 base nos seguintes casos, sempre escrevendo uma mensagem adequada:'''

import os
os.system('clear')

def flag(a,b,c):
	if a == b and b == c:
		return "TRIANGULO EQUILATERO"
	elif a == b or b == c:
		return "TRIANGULO ISOSCELES"


wert = input()

A, B, C = wert.split()
x = float(A)
y = float(B)
z = float(C)

listen = [x, y, z]
listen.sort(reverse=True)
a = listen[0]
b = listen[1]
c = listen[2]

if a >= (b + c):
	print("NAO FORMA TRIANGULO")
elif (a**2) == (b**2)+(c**2):
	print("TRIANGULO RETANGULO")
elif (a**2) > (b**2)+(c**2):
	print("TRIANGULO OBTUSANGULO")
	print(flag(a,b,c))
elif (a**2) < (b**2)+(c**2):
	print("TRIANGULO ACUTANGULO")
	print(flag(a,b,c))
