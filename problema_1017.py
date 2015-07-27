#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
os.system('clear')

def calgas(h,k):
	return (h * k)/12

h = int(input())
k = int(input())

print ("%.3f" %calgas(h,k))
