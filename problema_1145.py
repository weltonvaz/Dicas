#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""Escreva um programa que leia dois valores X e Y. A seguir, mostre uma
sequência de 1 até Y, passando para a próxima linha a cada X números."""

import os
os.system('clear')

N = input()

X,Y = N.split()

for i in range(1,int(Y)+1,int(X)):
    print(i,end=" ")
    for z in range(int(X)+1,int(X)+2):
        print(z)
