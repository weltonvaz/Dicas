#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos
(desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados."""

import os
os.system('clear')

a = input()
b = input()
c = input()
d = input()
e = input()
f = input()

lista = [a,b,c,d,e,f]
n = 6

for x in lista:
    if float(x) < 0:
        n-=1
print("%d valores positivos" %(n))
