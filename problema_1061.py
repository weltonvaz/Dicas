#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Pedrinho está organizando um evento em sua Universidade. O evento deverá ser
no mês de Abril, iniciando e terminando dentro do mês. O problema é que Pedrinho
quer calcular o tempo em segundos que o evento vai durar, uma vez que ele sabe
quando inicia e quando termina o evento. Sabendo que o evento pode durar de
poucos segundos a vários dias, você deverá ajudar Pedrinho a calcular a duração
deste evento."""

import os
os.system('clear')

diaN = int(input("Dia "))
horaN =  input()
diaF = int(input("Dia "))
horaF =  input()

hhN,mmN,ssN = horaN.split(":")
hhF,mmF,ssF = horaF.split(":")

W = int(diaF) - int(diaN)
X = int(hhF) - int(hhN)
Y = int(mmF) - int(mmN)
Z = int(ssF) - int(ssN)

print("%d dia(s)" %W)
print("%d hora(s)" %X)
print("%d minuto(s)" %Y)
print("%d segundo(s)" %Z)
