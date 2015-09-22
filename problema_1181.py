#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Neste problema você deve ler um número, indicando uma linha da matriz na
qual uma operação deve ser realizada, um caractere maiúsculo, indicando a
operação que será realizada, e todos os elementos de uma matriz M[12][12].
Em seguida, calcule e mostre a soma ou a média dos elementos que estão na área
verde da matriz, conforme for o caso. A imagem abaixo ilustra o caso da entrada
do valor 2 para a linha da matriz, demonstrando os elementos que deverão ser
considerados na operação."""

import os
os.system('clear')

def entrada():
    matriz = []
    for x in range(0,144):
        y = float(input())
        matriz.append(y)
    return matriz

def somam(valor):
    t = entrada()
    soma = 0
    for z in range(valor,144,12):
        soma = soma + t[z]
    return soma

def mediam(valor):
    t = entrada()
    media = 0
    soma = 0
    for z in range(valor,144,12):
        soma = (soma + t[z])
    media = soma/12
    return media

L = int(input())
while L < 0 or L > 11:
    L = int(input())

T = input()
while True:
    if T == 'S':
        print("%.1f" % somam(L))
        break
    elif T == 'M':
        print("%.1f" % mediam(L))
        break
    else:
        T = input()
