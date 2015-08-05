#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
os.system("clear")

def josephus(n, k=1):
	r = 0
	for i in range(1, n+1):
		r = (r+k)%i
	return int(r)+1

valor = input()
wert = []

for x in range(1,int(valor)+1):
	valores = input()
	a,b = valores.split()
	wert.append([x,int(a),int(b)])


for y in range(0,int(valor)):
	print("Case %d: %d" %(y+1,josephus(wert[y][1],wert[y][2])))
