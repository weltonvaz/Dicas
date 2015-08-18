#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 
até X, um valor por linha, inclusive o X, se for o caso."""

import os
os.system('clear')

X = int(input())
if X %2 != 0:
    X = X + 1

for x in range(1,X):
    if x % 2 != 0:
        print(x)