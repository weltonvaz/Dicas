#!/bin/python
# -*- coding: utf-8 -*-

import os
os.system("clear")

valor = input()

lista = []
wert = []

for x in range(1,int(valor)+1):
	valores = input()
	a,b = valores.split()
	wert.append([x,int(a),int(b)])

lista.extend(wert)

print(lista)
