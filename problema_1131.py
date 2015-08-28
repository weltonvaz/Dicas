#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""A Federação Gaúcha de Futebol contratou você para escrever um programa para
fazer uma estatística do resultado de vários GRENAIS. Escreva um programa para
ler o número de gols marcados pelo Inter e pelo Grêmio em um GRENAL. Logo após
escrever a mensagem "Novo grenal (1-sim 2-nao)" e solicitar uma resposta. Se a
resposta for 1, o algoritmo deve ser executado novamente solicitando o número de
gols marcados pelos times em uma nova partida, caso contrário deve ser encerrado
imprimindo:"""

import os
os.system('clear')

import sys

inter = 0
gremio = 0
empates = 0
timev = ""

def pergunta():
    global inter
    global gremio
    global empates
    global timev

    placar = input()
    i,g = placar.split()
    vermelho = int(i)
    azul = int(g)
    if vermelho > azul:
        inter += 1
    elif vermelho == azul:
        empates += 1
    else:
        gremio += 1
    answer()

def answer():
    answer = input("Novo grenal (1-sim 2-nao)\n")
    if answer == '1':
        pergunta()
    elif answer == '2':
        resposta()
        sys.exit()
    else:
        answer()

def resposta():
    total = inter+gremio+empates
    print("%d grenais" %total)
    print("Inter:%d" %inter)
    print("Gremio:%d" %gremio)
    print("Empates:%d" %empates)
    if inter > gremio:
        print("Inter venceu mais")
    elif inter == gremio:
        print("Nao houve vencedor")
    else:
        print("Gremio venceu mais")

pergunta()
