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

diaN = input()
horaN = input()
diaF = input()
horaF = input()

diasN,ddN = diaN.split(" ")
diasF,ddF = diaF.split(" ")
hhN,mmN,ssN = horaN.split(":")
hhF,mmF,ssF = horaF.split(":")

morgemN = int(ddN)
morgemF = int(ddF)

# TRABALHANDO COM DIAS
dia = morgemF - morgemN

# TRABALHANDO COM HORAS
if int(hhN) > int(hhF):
	hora = (24 + int(hhF)) - int(hhN)
	dia = dia - 1
elif int(hhN) <= int(hhF):
	hora = int(hhF) - int(hhN)

# TRABALHANDO COM MINUTOS
if int(mmN) > int(mmF):
	minutos = (60 + int(mmF)) - int(mmN)
elif int(mmN) <= int(mmF):
	minutos = int(mmF) - int(mmN)
	
# TRABALHANDO COM SEGUNDOS
if int(ssN) > int(ssF):
	segundos = (60 + int(ssF)) - int(ssN)
	minutos = minutos - 1
elif int(ssN) <= int(ssF):
	segundos = int(ssF) - int(ssN)
	
print("%d dia(s)" % dia)
print("%d hora(s)" % hora)
print("%d minuto(s)" % minutos)
print("%d segundo(s)" % segundos)

