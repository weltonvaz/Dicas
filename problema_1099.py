#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Leia um valor inteiro N que é a quantidade de casos de teste que vem a
seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar
 a soma de todos os ímpares existentes entre X e Y."""

import os
os.system('clear')

n = 1.0

for i in range(0,21,2):
    for j in range(1,4):
        if i == 0.0:
            print("I=%d J=%d" %(i,j))
        elif i == 1.0:
            print("I=%d J=%d" %(int(i),j))
        else:
            print("I=%.1f J=%s" %(i/10.0,(j+(i/10.0))))
