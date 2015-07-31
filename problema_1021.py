#!/bin/python
# -*- coding: utf-8 -*-

import os
os.system('clear')

troco = float(input())
notas = [100, 50, 20, 10, 5, 2]
moedas = [1,0.50,0.25,0.10,0.05,0.01]

if troco > 1:
	print("NOTAS:")
	for p in notas:
		if troco >= p:
			n = int(troco/p)
			r = troco - p*n
			print ('%s nota(s) de R$ %s.00' % (n, p))
			troco = r
		else:
			print ('0 nota(s) de R$ %s.00' %p)

resto = troco
	
if resto < 2.00:
	print("MOEDAS:")
	for p in moedas:
		if resto >= p:
			n = int(resto/p)
			r = resto - p*n
			print ('%s moeda(s) de R$ %.2f' % (n, p))
			resto = r
		else:
			print ('0 moeda(s) de R$ %.2f' %p)
