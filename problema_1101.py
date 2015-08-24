#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Leia um conjunto não determinado de pares de valores M e N (parar quando
 algum dos valores for menor ou igual a zero). Para cada par lido, mostre a
 sequência do menor até o maior e a soma dos inteiros consecutivos entre eles
 (incluindo o N e M). """

import os
os.system('clear')

while True:
    wert = input()
    M,N = wert.split()
    x = int(M)
    y = int(N)
    if x <= 0 or y <= 0:
        break
    else:
        folgenden = []
        snum = 0
        if x > y:
            for z in range(y,x+1):
                snum += z
                print(z,end=" ")

        else:
            for z in range(x,y+1):
                snum = snum + z
                print(z,end=" ")
        print("Sum=%d" %snum)
