
# -*- coding: utf-8 -*-

"""O programa deve ler um valor inteiro X indefinidas vezes. (O programa irá
parar quando o valor de X for igual a 0). Para cada X lido, imprima a soma dos
5 pares consecutivos a partir de X, inclusive o X , se for par. Se o valor de
entrada for 4, por exemplo, a saída deve ser 40, que é o resultado da operação:
4+6+8+10+12, enquanto que se o valor de entrada for 11, por exempo, a saída
deve ser 80, que é a soma de 12+14+16+18+20."""

import os
os.system('clear')

def spaare(x):
    soma = []
    if x % 2 != 0:
        x = x + 1
    for z in range(x,(x+10)):
        if z % 2 == 0:
            soma.append(z)
    return sum(soma)


while True:
    wert = int(input())
    if wert == 0:
        break
    else:
        print(spaare(int(wert)))
