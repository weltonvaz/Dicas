#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Maria acabou de iniciar seu curso de graduação na faculdade de medicina e
precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela
é responsável. Ela quer saber no final do ano, quantas cobaias foram utilizadas
no laboratório e o percentual de cada tipo de cobaia utilizada. Este laboratório
em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter
estas informações, ela sabe exatamente o número de experimentos que foram
realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em
cada experimento. """

import os
os.system('clear')

N = int(input())

count = 1
quantia = 0
coelho = 0
rato = 0
sapo = 0
cobaias = 0

while count <= N:
    quantia = input()
    valor,tipo = quantia.split()
    if tipo == 'C':
        coelho = coelho + int(valor)
    elif tipo == 'R':
        rato = rato + int(valor)
    elif tipo == 'S':
        sapo = sapo + int(valor)
    count += 1

cobaias = coelho+rato+sapo
perC = (coelho*100)/cobaias
perR = (rato*100)/cobaias
perS = (sapo*100)/cobaias

print("Total: %d cobaias" %cobaias)
print("Total de coelhos: %d" %coelho)
print("Total de ratos: %d" %rato)
print("Total de sapos: %d" %sapo)
print("Percentual de coelhos: %.2f %%" %(perC))
print("Percentual de ratos: %.2f %%" %(perR))
print("Percentual de sapos: %.2f %%" %(perS))
