
# -*- coding: utf-8 -*-

"""Faça um programa que leia um valor N. Este N será o tamanho de um vetor X[N].
A seguir, leia cada um dos valores de X, encontre o menor elemento deste vetor
e a sua posição dentro do vetor, mostrando esta informação."""

import os
os.system('clear')

N = int(input())
X = []
XX = []
y = 0

wert = input()

X = wert.split()

for z in X:
    if y <= N:
        XX.append(int(z))
        y += 1
menor = list(XX)
menor.sort()

for n in range(0,len(XX)):
    if XX[n] == menor[0]:
        print("Menor valor: %d" %XX[n])
        print("Posicao: %d" %n)
