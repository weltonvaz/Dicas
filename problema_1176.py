
# -*- coding: utf-8 -*-

"""Faça um programa que leia um valor e apresente o número de Fibonacci
correspondente a este valor lido. Lembre que os 2 primeiros elementos da série
de Fibonacci são 0 e 1 e cada próximo termo é a soma dos 2 anteriores a ele.
Todos os valores de Fibonacci calculados neste problema devem caber em um
inteiro de 64 bits sem sinal."""

import os
os.system('clear')

def fib(n, computed = {0: 0, 1: 1}):
    if n not in computed:
        computed[n] = fib(n-1, computed) + fib(n-2, computed)
    return computed[n]

T = int(input())
for x in range(0,T):
    N = int(input())
    print("Fib(%d) = %d" %(N,fib(N)))
