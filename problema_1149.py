#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""Faça um algoritmo para ler um valor A e um valor N. Imprimir a soma dos N
números a partir de A(inclusive). Enquanto N for negativo ou ZERO, um novo N
(apenas N) deve ser lido."""

import os
os.system('clear')

def maior(listas):
    for z in listas:
        if int(z) > 0:
            return z
lista = []
lista = input().split(" ")

if len(lista) == 2:
    A = int(lista[0])
    N = int(lista[1])
else:
    A = int(lista[0])
    lista.pop(0)
    N = int(maior(lista))

soma = 0

while(N > 0):
    N -= 1
    soma = soma + A
    A += 1

print(soma)
