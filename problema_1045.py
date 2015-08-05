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

listen = [x, y, z]
listen.sort(reverse=True)
a = listen[0]
b = listen[1]
c = listen[2]

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