ENTRADA = input()

NUMBER = ENTRADA.split()

NUMEROS = []
MAIORAB = 0

for x in NUMBER:
	NUMEROS.append(int(x))
NUMEROS.sort()

MAIORAB = int(((NUMEROS[2]+NUMEROS[1])+abs(NUMEROS[2]-NUMEROS[1]))/2)

print("%d eh o maior" %MAIORAB)

