#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""Faça um programa que leia dois inteiros: X e Z (devem ser lidos tantos
valores para Z quantos necessários, até que seja digitado um valor maior do que
X para ele). Conte quantos números inteiros devem ser somados em sequência
(considerando o X nesta soma) para que a soma ultrapasse a Z o mínimo possível.
Escreva o valor final da contagem. """

import os
os.system('clear')

X = int(input())
N = int(input())

while N <= X:
    N = int(input())

lista = []
lista.append(X)
soma = sum(lista)
while soma <= N:
    X = X+1
    lista.append(X)
    soma = sum(lista)
print(len(lista))
