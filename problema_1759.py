#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Papai Noel está brincando com seus duendes para entretê-los durante a véspera
do Natal. A brincadeira consiste nos elfos escreverem números em pedaços de
papel e colocarem no gorro do Papai Noel. Após todos terminarem de colocar os
números Noel sorteia um papel e aquele número representa quantos "Ho" o Noel
deve falar. Seu trabalho é ajudar o Papai Noel montando um problema que mostre
todos os "Ho" que ele deve falar dado o número sorteado."""

import os
os.system("clear")

T = int(input())

print("Ho",end="")

while T >= 2:
    print(" Ho",end="")
    T -= 1
print("!")
