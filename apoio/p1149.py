#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""Faça um algoritmo para ler um valor A e um valor N. Imprimir a soma dos N
números a partir de A(inclusive). Enquanto N for negativo ou ZERO, um novo N
(apenas N) deve ser lido."""

import os
os.system('clear')

A, N = [int(i) for i in input().split(" ")]

soma = 0

while(True):
   if((N <= 0)):
      N = int(input(""))
   else:
      break

while(N > 0):
   N -= 1
   soma = soma + A
   A += 1

print(soma)
