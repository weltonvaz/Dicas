
# -*- coding: utf-8 -*-

"""Na matemática, um Número Primo é aquele que pode ser dividido somente por 1
(um) e por ele mesmo. Por exemplo, o número 7 é primo, pois pode ser dividido
apenas pelo número 1 e pelo número 7."""

import os
os.system('clear')

def nperfect(n):
    divisores = []
    for x in range(1,n):
        if n % x == 0:
            divisores.append(x)
    if sum(divisores) == n:
        return "%d eh perfeito" %n
    else:
        return "%d nao eh perfeito" %n



N = int(input())

for z in range(0,N):
    X = int(input())
    print(nperfect(X))
