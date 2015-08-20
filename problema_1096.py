#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Você deve fazer um programa que apresente a sequencia conforme o exemplo
 abaixo."""

import os
os.system('clear')

for I in range(1,10,2):
    for J in reversed(range(5,8)):
        print("I=%d J=%d" %(I,J))
