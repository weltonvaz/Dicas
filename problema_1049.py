#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Neste problema você deverá ler 3 palavras que definem o tipo de
animal possível segundo o esquema abaixo, da esquerda para a direita.
Em seguida conclua qual dos animais seguintes foi escolhido, através
das três palavras fornecidas.
"""

import os
os.system('clear')

genero = input()
especie = input()
individuo = input()

if genero == "vertebrado":
    if especie == "ave":
        if individuo == "carnivoro":
            print("aguia")
        elif individuo == "onivoro":
            print("pomba")
    if especie == "mamifero":
        if individuo == "onivoro":
            print("homem")
        elif individuo == "herbivoro":
            print("vaca")
elif genero == "invertebrado":
    if especie == "inseto":
        if individuo == "hematofago":
            print("pulga")
        elif individuo == "herbivoro":
            print("lagarta")
    if especie == "anelideo":
        if individuo == "hematofago":
            print("sanguessuga")
        elif individuo == "onivoro":
            print("minhoca")



