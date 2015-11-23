#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um 
triângulo. Em caso positivo, calcule o perímetro do triângulo e 
apresente a mensagem:'''

import os
os.system('clear')

import math

def triangulo(a,b,c):
# Usando a formula de Heron
	Perimetro = (a + b + c)
	return Perimetro

def trapezio(a,b,c):
	Area = ((a + b) * c)/2
	return Area

wert = input()

A,B,C = wert.split()

a = float(A)
b = float(B)
c = float(C)

if (math.fabs(b - c)) < a < (b + c):
	print("Perimetro = %.1f" % triangulo(a,b,c))
elif (math.fabs(a - c)) < b < (a + c):
	print("Perimetro = %.1f" % triangulo(a,b,c))
elif (math.fabs(a - b)) < c < (a + b):
	print("Perimetro = %.1f" % triangulo(a,b,c))
else:
	print("Area = %.1f" %trapezio(a,b,c))

	


