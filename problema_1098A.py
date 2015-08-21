#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo."""

import os
os.system('clear')

i = 0
j = 1
n = 1.0

while i <= 2:
	if i % 1 == 0 and j % 1 == 0:
		print ("I=%d J=%d" % (i,j))
	elif  j % 1 == 0 and i %1 != 0:
		print ("I=%d J=%d" % (i,j))
	elif i % 1 == 0 and j % 1 != 0:
		print ("I=%d J=%d" % (i,j))
	else:
		print ("I=%.1f J=%.1f" %(i,j))
	j += 1
	if j > n+2:
		n += 0.2
		j = n
		i += 0.2
