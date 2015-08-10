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
x,y = punkt.split()

x = float(x)
y = float(y)
=======
X,Y = punkt.split()

x = float(X)
y = float(Y)
>>>>>>> 3667dc9d4596dbdfa96bbac9004212bc9aa7fd3e

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
else:
	if x == 0:
		print("Eixo X")
	elif y == 0:
		print("Eixo Y")
=======
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
>>>>>>> 3667dc9d4596dbdfa96bbac9004212bc9aa7fd3e
