ENTRADA = (input())

A,B,C = ENTRADA.split()

pi = 3.14159

TRIANGULO = (float(A) * float(C)) / 2
CIRCULO = pi * (float(C) ** 2)
TRAPEZIO = ((float(A) + float(B))/2)* float(C)
QUADRADO = float(B)**2
RETANGULO = float(A)*float(B)

print("TRIANGULO: %.3f" %TRIANGULO)
print("CIRCULO: %.3f" %CIRCULO)
print("TRAPEZIO: %.3f" %TRAPEZIO)
print("QUADRADO: %.3f" %QUADRADO)
print("RETANGULO: %.3f" %RETANGULO)
