#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem 
decrescente, de modo que o lado A representa o maior dos 3 lados. 
A seguir, determine o tipo de triângulo que estes três lados formam, com
 base nos seguintes casos, sempre escrevendo uma mensagem adequada:'''

import os

os.system('clear')

vert = input()

A, B, C = vert.split()

x = float(A)
y = float(B)
z = float(C)
<<<<<<< HEAD
	
=======

>>>>>>> 3667dc9d4596dbdfa96bbac9004212bc9aa7fd3e
listen = [x, y, z]
listen.sort(reverse=True)
a = listen[0]
b = listen[1]
c = listen[2]
<<<<<<< HEAD
	
if a >= (b + c):
	print("NAO FORMA TRIANGULO")
elif (a**2) == (b**2+c**2):
	print("TRIANGULO RETANGULO")
elif (a**2) > (b**2)+(c**2): 
	print("TRIANGULO OBTUSANGULO")
elif (a**2) < (b**2)+(c**2):
	print("TRIANGULO ACUTANGULO")


if a == b and a == c and b == c:
	print("TRIANGULO EQUILATERO")
elif a == b or a == c:
	print("TRIANGULO ISOSCELES")
elif b == a or b == c:
	print("TRIANGULO ISOSCELES")
=======

if a >= (b + c):
    print("NAO FORMA TRIANGULO")
elif (a**2) == (b**2+c**2):
    print("TRIANGULO RETANGULO")
elif (a**2) > (b**2+c**2):
    print("TRIANGULO OBTUSANGULO")
elif (a**2) < (b**2+c**2):
    print("TRIANGULO ACUTANGULO")
else:
    print("TRIANGULO NAO ENCONTRADO")

if a == b == c:
    print("TRIANGULO EQUILATERO")
else:
    print("TRIANGULO ISOSCELES")
>>>>>>> 3667dc9d4596dbdfa96bbac9004212bc9aa7fd3e
