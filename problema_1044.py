#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma 
mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores
 lidos são múltiplos entre si.'''

import os
os.system('clear')

def multiple(v, m):
    resto = v % m
    if resto == 0:
        return "Sao Multiplos"
    else:
        return "Nao sao Multiplos"

vert = input()

X,Y = vert.split()

lista = [int(X),int(Y)]

print(multiple(max(lista),min(lista)))
