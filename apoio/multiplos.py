def multiplo(n):
 for x in range(1, n):
  if (n % x == 0): #se o resto da divisão de n/x for 0 (múltiplo)
   print (x) #múltiplo

n = int(input())
print(multiplo(n))
