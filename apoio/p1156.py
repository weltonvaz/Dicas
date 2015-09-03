soma = 0
j = 1.00

for i in range(1,40,2):
    aux = (i/j)
    soma += aux
    j = j*2

print("%.2f" %soma)
