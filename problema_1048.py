#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' A empresa ABC resolveu conceder um aumento de salários a seus 
funcionários de acordo com a tabela abaixo:'''

import os
os.system('clear')

<<<<<<< HEAD
=======
def aumento(salario,indice):
	nsalario = salario*indice
	dsalario = nsalario - salario
	return "Novo salario: %.2f\nReajuste ganho: %.2f" % (nsalario,dsalario)


salario = float(input())

if salario <= 400.00:
	print(aumento(salario,1.15))
	print("Em percentual: 15 %")
elif salario <= 800.00:
	print(aumento(salario,1.12))
	print("Em percentual: 12 %")
elif salario <= 1200.00:
	print(aumento(salario,1.10))
	print("Em percentual: 10 %")
elif salario <= 2000.00:
	print(aumento(salario,1.07))
	print("Em percentual: 7 %")
else:
	print(aumento(salario,1.04))
	print("Em percentual: 4 %")

>>>>>>> ea18cdfcc12bdfc2cd07b79cd9e7a09cc388430a
