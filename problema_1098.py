#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Você deve fazer um programa que apresente a sequencia conforme o exemplo
 abaixo."""

import os
os.system('clear')

lista1 = [7,6,5,9,8,7,11,10,9,13,12,11,15,14,13]
lista2 = [1,1,1,3,3,3,5,5,5,7,7,7,9,9,9]

for x in range(0,15):
    print("I=%d J=%d" %(lista2[x],lista1[x]))
