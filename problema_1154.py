#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""Faça um algoritmo para ler um número indeterminado de dados, contendo cada um
, a idade de um indivíduo. O último dado, que não entrará nos cálculos, contém o
valor de idade negativa. Calcular e imprimir a idade média deste grupo de
 indivíduos."""

import os
os.system('clear')

def midade(lista):
    soma = sum(lista)
    media = soma/len(lista)
    return media

idades = []
while True:
    i = int(input())
    if i >= 0:
        idades.append(i)
    else:
        break
print("%.2f" %(midade(idades)))
