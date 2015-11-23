#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Problema de crescimento populacional
# Desenvolvido por Evaldo Junior (InFog)
# http://evaldojunior.com.br/blog
import os
os.system('clear')

import math

popA, popB, anos = 100, 150, 0
cresA, cresB = 1.0, 0
while (popB >= popA):
    anos += 1
    popA = math.trunc(popA + (popA * (cresA/100)))
    popB = math.trunc(popB + (popB * (cresB/100)))
    print(popA,popB,anos)

print("Após %i anos o país A ultrapassou o país B em número de habitantes." % anos)
print("País A: %.0f" % popA)
print("País B: %.0f" % popB)
