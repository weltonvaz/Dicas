#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Faça um programa que leia 5 valores inteiros. Conte quantos destes valores
digitados são pares e mostre esta informação."""

import os
os.system('clear')

pares = 0
for x in range(0,5):
    x = int(input())
    if x % 2 == 0:
        pares += 1

print ("%d valores pares" %pares)
