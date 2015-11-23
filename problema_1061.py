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

diaN = int(input("Dia "))
horaN =  input()
diaF = int(input("Dia "))
horaF =  input()

hhN,mmN,ssN = horaN.split(":")
hhF,mmF,ssF = horaF.split(":")

data1 = datetime(2015,8,int(diaN),int(hhN),int(mmN),int(ssN))
data2 = datetime(2015,8,int(diaF),int(hhF),int(mmF),int(ssF))

difdata = data2 - data1
datatt = '{0}:{2}'.format(*str(difdata).split())

W,X,Y,Z = datatt.split(":")

print("%s dia(s)" %int(W))
print("%s hora(s)" %int(X))
print("%s minuto(s)" %int(Y))
print("%s segundo(s)" %int(Z))
