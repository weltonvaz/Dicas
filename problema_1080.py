#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Leia 100 valores inteiros. Apresente então o maior valor lido e a posição
dentre os 100 valores lidos. """

import os
os.system('clear')

def indice(listas, maior):
    posicao = 0
    for index in len(listas):
        if index == maior:
            posicao = index
    return posicao

lista = []
count = 0

while count <= 3:
    wert = int(input())
    lista.append(wert)
    count += 1

maior = 0

for x in lista:
    if x > maior:
        maior = x
print(maior)
print(indice(lista,maior))
