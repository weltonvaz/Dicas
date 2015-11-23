#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Leia um valor inteiro N que é o tamanho da matriz que deve ser impressa
conforme o modelo fornecido. """
import os
os.system("clear")

while True:
    try:
        N = int(input())
        if N < 3 or N > 70:
            break
        else:
            for i in range(0,N):
                for j in range(0,N):
                    if i == j and i + j == N-1:
                        print("2",end="")
                    elif (i == j):
                        print("1",end="")
                    elif (i + j == N-1):
                        print("2",end="")
                    else:
                        print("3",end="")
                print()
    except EOFError:
        break
    except ValueError:
        break
