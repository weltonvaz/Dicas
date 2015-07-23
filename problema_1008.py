a = input()
b = input()

prod1 = a.split()
prod2 = b.split()

total = (float(prod1[1]) * float(prod1[2])) + (float(prod2[1]) * float(prod2[2]))


print("VALOR A PAGAR: R$ %.2f" %total)
