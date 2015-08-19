#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Leia um valor inteiro N. Apresente todos os números entre 1 e 10000 que
divididos por N dão resto igual a 2."""

import os
os.system('clear')

N = int(input())

for x in range(1,10000):
    if x % N == 2:
        print(x)
