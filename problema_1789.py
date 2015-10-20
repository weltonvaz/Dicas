#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""A corrida de lesmas é um esporte que cresceu muito nos últimos anos, fazendo
com que várias pessoas dediquem suas vidas tentando capturar lesmas velozes, e
treina-las para faturar milhões em corridas pelo mundo. Porém a tarefa de
capturar lesmas velozes não é uma tarefa muito fácil, pois praticamente todas as
lesmas são muito lentas. Cada lesma é classificada em um nível dependendo de sua
velocidade:"""

import os
os.system("clear")

import sys

def maior(lista):
    velox = lista[1::2]
    indix = velox.index(max(lista[1::2]))
    return indix + 1

L = int(input())
vi = []
vo = []

wert = input()
vi = wert.split()

for x in vi:
    vo.append(int(x))

print(maior(vo))
