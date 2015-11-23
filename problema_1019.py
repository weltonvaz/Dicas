#!/bin/python
# -*- coding: utf-8 -*-

import os
os.system('clear')

segundos = int(input())

horas = segundos//3600
minutos = (segundos-(horas*3600))//60
segundos = segundos-(horas*3600)-(minutos*60)
      
print("%d:%d:%d" %(horas,minutos,segundos))
