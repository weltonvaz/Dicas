#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Com base na tabela abaixo, escreva um programa que leia o código de
um item e a quantidade deste item.
A seguir, calcule e mostre o valor da conta a pagar.'''

import os
os.system('clear')

valores = input()
preis = 0

a,b = valores.split()

if a == "1":
	preis = float(b) * 4.00
elif a == "2":
	preis = float(b) * 4.50
elif a == "3":
	preis = float(b) * 5.00
elif a == "4":
	preis = float(b) * 2.00
elif a == "5":
	preis = float(b) * 1.50
else:
	print("Código não existe")

print("Total: R$ %.2f" %preis)
