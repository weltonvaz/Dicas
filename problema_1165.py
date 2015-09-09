
# -*- coding: utf-8 -*-

"""Na matemática, um Número Primo é aquele que pode ser dividido somente por 1
(um) e por ele mesmo. Por exemplo, o número 7 é primo, pois pode ser dividido
apenas pelo número 1 e pelo número 7."""

import os
os.system('clear')

def eprimo(n):
    divisores = []
    for x in range(1,n+1):
        if n % x == 0:
            divisores.append(x)
    if len(divisores) == 2:
        return "%d eh primo" %n
    else:
        return "%d nao eh primo" %n

N = int(input())

for z in range(0,N):
    X = int(input())
    print(eprimo(X))
