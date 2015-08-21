#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo."""

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
