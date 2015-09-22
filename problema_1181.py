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
    """matriz = []
    for x in range(0,144):
        y = float(input())
        matriz.append(y)"""
    matriz = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144]
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
