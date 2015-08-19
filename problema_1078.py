#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Leia 1 valor inteiro N (2 < N < 1000). A seguir, mostre a tabuada de N:
1 x N = N      2 x N = 2N        ...       10 x N = 10N"""

import os
os.system('clear')

N = int(input())

for x in range(1,11):
    total = N * x
    print("%d x %d = %d" %(x,N,total))
