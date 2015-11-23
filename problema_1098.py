#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo."""

import os
os.system('clear')

n = 0.0

for i in range(0,3):
    for j in range(1,4):
        if i == 0.0:
            print(i,j)
        else:
            print(i+n,j+n)
    n += 0.2
