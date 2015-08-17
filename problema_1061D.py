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

import datetime

diaN = input()
horaN = input()
diaF = input()
horaF = input()

diasN,ddN = diaN.split(" ")
diasF,ddF = diaF.split(" ")
hhN,mmN,ssN = horaN.split(":")
hhF,mmF,ssF = horaF.split(":")

s = str((ddN+"/4/2015 ")+(hhN.strip()+":"+mmN.strip()+":"+ssN.strip()))
t = str((ddF+"/4/2015 ")+(hhF.strip()+":"+mmF.strip()+":"+ssF.strip()))

date1 = int(datetime.datetime.strptime(s, '%d/%m/%Y %H:%M:%S').strftime("%s"))
date2 = int(datetime.datetime.strptime(t, '%d/%m/%Y %H:%M:%S').strftime("%s"))

difdate = date2 - date1

dia = divmod(difdate,86400)
hora = divmod(dia[1],3600)
minuto = divmod(hora[1],60)
segundo = divmod(minuto[1],60)

print("%s dia(s)" %str(dia[0]))
print("%s hora(s)" %str(hora[0]))
print("%s minuto(s)" %str(minuto[0]))
print("%s segundo(s)" %str(segundo[1]))
