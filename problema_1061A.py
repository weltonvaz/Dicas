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

from datetime import datetime

diaN = input()
horaN = input()
diaF = input()
horaF = input()

diasN,ddN = diaN.split(" ")
diasF,ddF = diaF.split(" ")
hhN,mmN,ssN = horaN.split(":")
hhF,mmF,ssF = horaF.split(":")

data1 = datetime(2015, 8, int(ddN),int(hhN),int(mmN),int(ssN))
data2 = datetime(2015, 8, int(ddF),int(hhF),int(mmF),int(ssF))
difdata = data2 - data1
datatt = '{0}:{4}'.format(*str(difdata).split())

print(datatt)

"""dia,hora,minuto,segundo = datatt.split(":")

print("%d dia(s)" % int(dia))
print("%d hora(s)" % int(hora))
print("%d minuto(s)" % int(minuto))
print("%d segundo(s)" % int(segundo))"""

