#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Leia um valor inteiro N. Apresente o quadrado de cada um dos valores pares,
de 1 até N, inclusive N, se for o caso."""

import os
os.system('clear')

N = int(input())

while N < 5 or N > 2000:
    N = int(input())

if N % 2 != 0:
    for x in range(2,N+1,2):
            print("%d^2 = %d" %(x,x**2))
else:
    for x in range(2,N+1,2):
            print("%d^2 = %d" %(x,x**2))
