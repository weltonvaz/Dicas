import datetime
import time

diaN = input()
horaN = input()
diaF = input()
horaF = input()

diasN,ddN = diaN.split(" ")
diasF,ddF = diaF.split(" ")
hhN,mmN,ssN = horaN.split(" : ")
hhF,mmF,ssF = horaF.split(" : ")

print(hhN,mmN,ssN)
print(hhF,mmF,ssF)

s = str(ddN+"/8/2015 "+(hhN+":"+mmN+":"+ssN))
t = str(ddF+"/8/2015 "+(hhF+":"+mmF+":"+ssF).rstrip(" "))

print(s)
print(t)
