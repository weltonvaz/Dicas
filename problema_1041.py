#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Leia 2 valores com uma casa decimal (x e y), que devem representar as
coordenadas de um ponto em um plano. A seguir, determine qual o
quadrante ao qual pertence o ponto, ou se está sobre um dos eixos
cartesianos ou na origem (x = y = 0).'''

punkt = input()
<<<<<<< HEAD

=======
 
>>>>>>> 261f8e1fb5949d284dc88e03c14fc076ec8b61a7
X,Y = punkt.split()
 
x = float(X)
y = float(Y)
<<<<<<< HEAD

=======
 
>>>>>>> 261f8e1fb5949d284dc88e03c14fc076ec8b61a7
if (x == 0 and y == 0):
    print("Origem")
elif (x == 0):
    print("Eixo Y")
elif (y == 0):
    print("Eixo X")
elif (x > 0 and y > 0):
    print("Q1")
elif (x < 0 and y > 0):
    print("Q2")
elif (x < 0 and y < 0):
    print("Q3")
else:
    print("Q4")
