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

def maior(lista):
    velox = max(lista)
    if velox < 10:
        return 1
    elif velox >= 10 and velox < 20:
        return 2
    else:
        return 3

while True:
    try:
        L = int(input())
        vi = []
        vo = []

        wert = input()
        vi = wert.split()

        for x in range(0,L):
            vo.append(int(vi[x]))

        print(maior(vo))
    except EOFError:
        break
    except ValueError:
        break
