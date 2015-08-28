#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""Escreva um programa que leia um valor inteiro N. Este N é a quantidade de
linhas de saída que serão apresentadas na execução do programa."""

import os
os.system('clear')

N = int(input())
for i in range(1,N+1):
    a = 0
    b = 0
    c = 0
    d = 0
    a=i*i
    b=i*i*i
    print("%d %d %d" %(i,a,b))
    c=i*i+1
    d=i*i*i+1
    print("%d %d %d" %(i,c,d))
