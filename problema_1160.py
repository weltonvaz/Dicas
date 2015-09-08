
# -*- coding: utf-8 -*-

"""Mariazinha quer resolver um problema interessante. Dadas as informações de
população e a taxa de crescimento de duas cidades quaisquer (A e B), ela
gostaria de saber quantos anos levará para que a cidade menor (sempre é a
cidade A) ultrapasse a cidade B em população. Claro que ela quer saber apenas
para as cidades cuja taxa de crescimento da cidade A é maior do que a taxa de
crescimento da cidade B, portanto, previamente já separou para você apenas os
casos de teste que tem a taxa de crescimento maior para a cidade A. Sua tarefa
é construir um programa que apresente o tempo em anos para cada caso de teste.
Porém, em alguns casos o tempo pode ser muito grande, e Mariazinha não se
interessa em saber exatamente o tempo para estes casos. Basta que você informe,
nesta situação, a mensagem "Mais de 1 seculo."""

import os
os.system('clear')

import math

def bevolkerung(popA,popB,cresA,cresB):
    anos = 0
    while (popA < popB):
            anos += 1
            popA = math.fabs(popA + (popA * (cresA/100)))
            popB = math.fabs(popB + (popB * (cresB/100)))
    if anos > 100:
        return "Mais de 1 seculo."
    else:
        return "%d anos." %anos

T = int(input())

for i in range(0,T):
    wert = input()
    x,y,z,i = wert.split()
    PA = int(x)
    PB = int(y)
    G1 = float(z)
    G2 = float(i)
    if PA < PB:
        print(bevolkerung(PA,PB,G1,G2))
    else:
        print(bevolkerung(PB,PA,G2,G1))
