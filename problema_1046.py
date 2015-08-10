#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Leia a hora inicial e a hora final de um jogo. A seguir calcule a duração do jogo, sabendo que o mesmo pode começar
em um dia e terminar em outro, tendo uma duração mínima de 1 hora e máxima de 24 horas.'''

import os
os.system('clear')

vert = input()

A, B = vert.split()

x = int(A)
y = int(B)

if x > y:
	t = (24 + y) - x
	print("O JOGO DUROU %d HORA(S)" % t)
elif x < y:
	t = y - x
	print("O JOGO DUROU %d HORA(S)" % t)
else:
	print("O JOGO DUROU 24 HORA(S)")

