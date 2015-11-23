#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''A entrada contém quatro números de ponto flutuante correspendentes as
notas dos alunos.'''

import os
os.system('clear')

def recupera(MP,NE):
	MPE = (MP+NE)/2
	return MPE	
	
valores = input()

N1,N2,N3,N4 = valores.split()

MP = ((float(N1)*2 + float(N2)*3 + float(N3)*4 + float(N4)*1))/(1+2+3+4)

if MP >= 7.0:
	print("Media: %.1f" %MP)
	print("Aluno aprovado.")
elif 9.0 >= MP >= 5.0:
	print("Media: %.1f" %MP)	
	print("Aluno em exame.")
	NE = input()
	print("Nota do exame: %.1f" %(float(NE)))
	NotaE = recupera(float(MP),float(NE))
	if NotaE >= 5.0:
		print("Aluno aprovado.\nMedia final: %.1f" %NotaE)
	else:
		print("Aluno reprovado.\nMedia final: %.1f" %NotaE)	
else:
	print("Media: %.1f" %MP)
	print("Aluno reprovado.")
	






