#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
os.system('clear')

import math
user = -1
 
while user != 0:
	user = int(input())
	while user > 100 or user < 0:
		user = int(input())
	if user <= 2:
		matrix = [[(1) for row in range(user)] for column in range(user)]
	else:
		matrix = [[(0) for row in range(user)] for column in range(user)]
		ceiling = int(math.ceil(user/2.0))
		for c in range(1, ceiling + 1):
			for i in range(user):
				for j in range(user):
					if (((i == c -1) or (i == user - c)) or ((j == c - 1) or (j == user - c))):
						if matrix[i][j] < 1:
							matrix[i][j] = c

	print(matrix)
			
