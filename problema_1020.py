#!/bin/python
# -*- coding: utf-8 -*-

import os
os.system('clear')

dias = int(input())

ano = dias//365
meses = (dias-(ano*365))//30
dia = dias-(ano*365)-(meses*30)
      
print("%d ano(s)" %(ano))
print("%d mes(es)" %(meses))
print("%d dia(s)" %(dia))
