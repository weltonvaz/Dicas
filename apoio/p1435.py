#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
os.system('clear')

n = int(input())
while True:
	if (n == 0):
		break
	k = n % 2
	m = n / 2
	
	nl = 1
	q = n
	
	for i in range(1, n+1):
		np = 1
		p = 0
		
		for j in range(0,n):
			if j ==  0:
				print(" ")
			else:
				print("  ")
			if (p == 0 and np != nl):
				if (np < 10):
					print(" ")
					print(np)
				elif (np == nl and p < q):
					if (nl < 10):
						print(" ")
						print(nl)
					p += 1
				else:
					np -= 1
					if (np < 10):
						print(" ")
					print(np)
		if (i < m):
			nl += 1
			q -= 2
		elif (i == m and k == 1):
			nl += 1
			q = 1
		elif (i == m and k == 0):
			q = 2
		else:
			q += 2
			nl -= 1
        
