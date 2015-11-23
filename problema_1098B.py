#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo."""

import os
os.system('clear')

i = [0,0,0,0.2,0.2,0.2,0.4,0.4,0.4,0.6,0.6,0.6,0.8,0.8,0.8,1,1,1,1.2,1.2,1.2,1.4,1.4,1.4,1.6,1.6,1.6,1.8,1.8,1.8,2,2,2]
j = [1,2,3,1.2,2.2,3.2,1.4,2.4,3.4,1.6,2.6,3.6,1.8,2.8,3.8,2,3,4,2.2,3.2,4.2,2.4,3.4,4.4,2.6,3.6,4.6,2.8,3.8,4.8,3,4,5]

for x in range(0,len(i)):
    print("I=%s J=%s" %(i[x],j[x]))
