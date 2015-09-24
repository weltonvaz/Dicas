import os
os.system('clear')

def soma(N):
	somam = 0
	matriz = []
	for i in range(0,12):
		for j in range(0,12):
			M = float(input())
			matriz.append(M)
			if i == N:
				somam += M
	return somam
	
N = int(input())
T = input()
if (T == 'S'):
	print("%.1f" %soma(N))
else:
	media = soma(N)
	print("%.1f" %(media/12.0))
