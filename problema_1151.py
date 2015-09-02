#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série
de Fibonacci. Nessa sequência, cada número, depois dos 2 primeiros, é igual à
soma dos 2 anteriores. Escreva um algoritmo que leia um inteiro N (N < 46) e
mostre os N primeiros números dessa série."""

import os
os.system('clear')

def fib(n):
    fibo = []
    a, b = 0, 1
    while a < n:
        fibo.append(a)
        a, b = b, a+b
    for z in fibo:
        print(z,end=' ')
    return ''

num = int(input())
fib(num)
