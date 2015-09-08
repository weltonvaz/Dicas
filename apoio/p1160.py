#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Problema de crescimento populacional
# Desenvolvido por Evaldo Junior (InFog)
# http://evaldojunior.com.br/blog
import os
os.system('clear')

import math

popA, popB, anos = 90000, 120000, 0
cresA, cresB = 5.5, 3.5
while (popA < popB):
    anos += 1
    popA = math.fabs(popA + (popA * (cresA/100)))
    popB = math.fabs(popB + (popB * (cresB/100)))
print("Após %i anos o país A ultrapassou o país B em número de habitantes." % anos)
print("País A: %.0f" % popA)
print("País B: %.0f" % popB)
