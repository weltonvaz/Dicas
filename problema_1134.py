#!/usr/local/bin/python
# -*- coding: utf-8 -*-

"""Um Posto de combustíveis deseja determinar qual de seus produtos tem a
preferência de seus clientes. Escreva um algoritmo para ler o tipo de
combustível abastecido (codificado da seguinte forma: 1.Álcool 2.Gasolina
3.Diesel 4.Fim). Caso o usuário informe um código inválido (fora da faixa de 1
a 4) deve ser solicitado um novo código (até que seja válido). O programa será
encerrado quando o código informado for o número 4."""

import os
os.system('clear')

import sys

Alcool = 0
Gasolina = 0
Diesel = 0

def kraftstoff():
    global Alcool
    global Gasolina
    global Diesel

    x = int(input())
    if x == 1:
        Alcool += 1
    elif x == 2:
        Gasolina += 1
    elif x == 3:
        Diesel += 1
    elif x == 4:
        antwort()
        sys.exit()
    else:
        kraftstoff()

def antwort():
    print("MUITO OBRIGADO")
    print("Alcool: %d" %Alcool)
    print("Gasolina: %d" %Gasolina)
    print("Diesel: %d" %Diesel)

while True:
    kraftstoff()
