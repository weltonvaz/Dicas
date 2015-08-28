#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""Escreva um programa que leia um valor inteiro N. Este N é a quantidade de
linhas de saída que serão apresentadas na execução do programa."""

import os
os.system('clear')

import math

N = int(input())

for x in range(1,(N)+1):
    print("%d %d %d" %(x,x**2,(pow(x,3))))
