#!/bin/python
# -*- coding: iso-8859-15 -*-
#contador de troco

import os
os.system('clear')

troco = int(input())
print("\n")
moedas = [100, 50, 20, 10, 5, 2, 1]

if troco > 0:
	print(troco,"\n")
	for p in moedas:
		if troco >= p:
			n = int(troco/p)
			r = troco - p*n
			print ('%s nota(s) de R$ %s' % (n, p))
			troco = r
		else:
			print ('0 nota(s) de R$ %s' %p)
		
