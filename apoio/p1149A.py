import os
os.system('clear')

def maior(listas):
	for z in listas:
		if int(z) > 0:
			return z
		

lista = []
lista = input().split(" ")
A = int(lista[0])
lista.pop(0)
print(maior(lista))

