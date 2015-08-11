#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Leia 2 valores com uma casa decimal (x e y), que devem representar as
coordenadas de um ponto em um plano. A seguir, determine qual o 
quadrante ao qual pertence o ponto, ou se está sobre um dos eixos 
cartesianos ou na origem (x = y = 0).'''

import os
os.system('clear')

punkt = input()

<<<<<<< HEAD
=======
<<<<<<< HEAD
x,y = punkt.split()

x = float(x)
y = float(y)
=======
>>>>>>> ea18cdfcc12bdfc2cd07b79cd9e7a09cc388430a
X,Y = punkt.split()

x = float(X)
y = float(Y)
<<<<<<< HEAD
=======
>>>>>>> 3667dc9d4596dbdfa96bbac9004212bc9aa7fd3e
>>>>>>> ea18cdfcc12bdfc2cd07b79cd9e7a09cc388430a

if x == 0 and y == 0:
	print("Origem")
elif x > 0 and y > 0:
	print("Q1")
elif x > 0 and y < 0:
	print("Q4")
elif x < 0 and y > 0:
	print("Q2")
elif x < 0 and y < 0:
	print("Q3")
<<<<<<< HEAD
=======
<<<<<<< HEAD
else:
	if x == 0:
		print("Eixo X")
	elif y == 0:
		print("Eixo Y")
=======
>>>>>>> ea18cdfcc12bdfc2cd07b79cd9e7a09cc388430a
elif x == 0 and y > 0:
	print("Eixo X")
elif x == 0 and y < 0:
	print("Eixo X")
elif y == 0 and x > 0:
	print("Eixo Y")
elif y == 0 and x < 0:
	print("Eixo Y")	
else:
	print()
<<<<<<< HEAD
=======
>>>>>>> 3667dc9d4596dbdfa96bbac9004212bc9aa7fd3e
>>>>>>> ea18cdfcc12bdfc2cd07b79cd9e7a09cc388430a
