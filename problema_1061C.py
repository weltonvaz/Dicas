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
dia, hora, minutos, segundos = 0

# TRABALHANDO COM DIAS
dia = morgemF - morgemN
if dia < 0:
	dia = 0
	hora = hora + 24

# TRABALHANDO COM HORAS
hora = (int(hhF) - int(hhN)) + hora
if hora < 0:
	hora = 0
elif hora > 24:
	hora = 0
		
	
# TRABALHANDO COM MINUTOS
minutos = (int(mmF) - int(mmN)) 
if minutos >= 60:
	minutos == 0
	segundos = segundos + 60
else minutos > 0:
	minutos == 0
	
# TRABALHANDO COM SEGUNDOS
segundos = (int(ssF) - int(ssN))
	
print("%d dia(s)" % dia)
print("%d hora(s)" % hora)
print("%d minuto(s)" % minutos)
print("%d segundo(s)" % segundos)

