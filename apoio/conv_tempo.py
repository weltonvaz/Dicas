#!/usr/bin/env python
# -*- coding: utf-8 -*-

#("***Calcular Tempo de Evento***")
 
import os
os.system('clear')

totalSegundos = int(input("Informe o tempo em segundos -"))

horas = totalSegundos / 360

sobraHoras = totalSegundos - (horas * 360)

minutos = sobraHoras / 60

segundos = sobraHoras - (minutos * 60)

print("Tempo do Evento: ", horas, "h", minutos, "min", segundos, "seg")

