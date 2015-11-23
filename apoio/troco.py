#!/bin/python
# -*- coding: iso-8859-15 -*-
#contador de troco

import os
os.system('clear')

moedas = {200: "2 euros", 100: "1 euro", 50: "50 cêntimos", 20: "20 cêntimos", 10: "10 cêntimos", 5: "5 cêntimos", 2: "2 cêntimos", 1: "1 cêntimo"]
valor = int(raw_input("Insira o valor a devolver ao cliente em cêntimos: "))

troco = {}
for moeda in moedas:
    if valor == 0: break
    while valor >= moeda:
        try: troco[moeda] += 1
        except KeyError: troco[moeda] = 1

if troco == {}:
    if valor != 0: print "Não temos moedas para fazer o troco."
    else: print "Não é suposto dar troco..."
else:
    if valor != 0: print "Não temos moedas para fazer o troco certo, estamos a dever %i cêntimos." % valor
    print "Troco:"
    for moeda in troco:
        print "%i moeda(s) de %s" % (troco[moeda], moedas[moeda])
