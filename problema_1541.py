
""" Considere que ele tenha por exemplo, um projeto para construir uma casa de 8
metros por 10 metros e a legislação do município permite construir no máximo de
100% do terreno. Como todos os terrenos nesta cidade são perfeitamente quadrados
e o valor dos lados da casa são apenas uma referência para a área total a ser
construída (80 metros quadrados), o sr PI precisaria de um terreno de 8.994
metros, o que truncado daria como resultado 8 metros e o tamanho real da casa
seria 64 metros quadrados. Se a legislação permitisse construir em 50% do
terreno, o terreno teria que ter 160 metros para que 50% dele fosse 80 metros
quadrados, o suficiente para uma casa de 8 x 8 metros (64 metros quadrados).
No primeiro caso de teste, como o percentual para construir é de apenas 20%, o
terreno teria que ter 20 metros de lado para que 1/5 deste terreno tenha tamanho
de 80 metros quadrados.
Ajude o sr PI a determinar o tamanho minimo do terreno."""

import os
os.system("clear")

import math

while True:
    wert = input()
    if wert == 0 or wert == "0":
        break
    else:
        A,B,C = wert.split()

        a = int(A)
        b = int(B)
        c = int(C)

        minimun_land_size = (100 * a * b) / c
        print(int(math.sqrt(minimun_land_size)))
