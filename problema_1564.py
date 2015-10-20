#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" O Brasil é o país sede da copa esse ano. Porém, há muitas pessoas
protestando contra o governo. Em redes sociais é possível ver pessoas afirmando
que não vai ter copa devido aos protestos.

Mas esses rumores de que não haverá copa são totalmente falsos, a presidente
Dilma Roussef já avisou: vai ter copa sim, e se reclamar vai ter duas!"""

import os
os.system("clear")
N = 0
while N >= 0 or N <= 100:
    try:
        N = int(input())
        if N == 0:
            print("vai ter copa!")
        else:
            print("vai ter duas!")
    except EOFError:
        break
    except ValueError:
        break
