#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""Escreva um programa que leia um valor inteiro N. Este N é a quantidade de
linhas de saída que serão apresentadas na execução do programa."""

import os
os.system('clear')

N = int(input())

for x in range(1,(N*4)+1):
    if x % 4 == 0:
        print("PUM \n")
    print(x,end=" ")
