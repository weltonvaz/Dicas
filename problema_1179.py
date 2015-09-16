
# -*- coding: utf-8 -*-

"""Neste problema você deverá ler 15 valores colocá-los em 2 vetores conforme
estes valores forem pares ou ímpares. Só que o tamanho de cada um dos dois
vetores é de 5 posições. Então, cada vez que um dos dois vetores encher, você
deverá imprimir todo o vetor e utilizá-lo novamente para os próximos números
que forem lidos. Terminada a leitura, deve-se imprimir o conteúdo que restou em
cada um dos dois vetores, imprimindo primeiro os valores do vetor impar. Cada
vetor pode ser preenchido tantas vezes quantas for necessário."""

import os
os.system('clear')

def imp_par(pares):
    for p in range(0,5):
        print("par[%d] = %d" %(p,pares[p]))

def imp_impar(impares):
    for p in range(0,5):
        print("impar[%d] = %d" %(p,impares[p]))

par = []
impar = []

for z in range(0,15):
    wert = int(input())
    if wert % 2 == 0:
        par.append(wert)
        if len(par) >= 5:
            imp_par(par)
            par = []
    elif wert % 2 != 0:
        impar.append(wert)
        if len(impar) >= 5:
            imp_impar(impar)
            impar = []
for i in range(0,len(impar)):
    print("impar[%d] = %d" %(i,impar[i]))
for p in range(0,len(par)):
    print("par[%d] = %d" %(p,par[p]))
