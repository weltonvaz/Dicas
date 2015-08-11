#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Em um país imaginário denominado Lisarb, todos os habitantes ficam felizes em pagar seus impostos,
pois sabem que nele não existem políticos corruptos e os recursos arrecadados são utilizados em
benefício da população, sem qualquer desvio. A moeda deste país é o Rombus, cujo símbolo é o R$.
Leia um valor com duas casas decimais, equivalente ao salário de uma pessoa de Lisarb. Em seguida,
calcule e mostre o valor que esta pessoa deve pagar de Imposto de Renda, segundo a tabela abaixo."""

import os
os.system('clear')

rombus = float(input())

if rombus <= 2000.00:
    print("Isento")
elif rombus <= 3000.00:
    imposto = (rombus - 2000.00) * 0.08
    print("R$ %.2f" % imposto)
elif rombus <= 4500.00:
    faixa1 = 80.00
    imposto = ((rombus - 3000.00) * 0.18) + faixa1
    print("R$ %.2f" % imposto)
elif rombus > 4500.00:
    faixa2 = 350.00
    imposto = ((rombus - 4500.00) * 0.28) + faixa2
    print("R$ %.2f" % imposto)
