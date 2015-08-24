#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Escreva um programa que repita a leitura de uma senha até que ela seja
válida. Para cada leitura de senha incorreta informada, escrever a mensagem
"Senha Invalida". Quando a senha for informada corretamente deve ser impressa a
mensagem "Acesso Permitido" e o algoritmo encerrado. Considere que a senha
correta é o valor 2002."""

import os
os.system('clear')


while True:
    senha = input()
    if senha == '2002':
        print("Acesso Permitido")
        break
    else:
        print("Senha Invalida")
