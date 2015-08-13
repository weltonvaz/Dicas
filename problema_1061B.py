diaN = int(input())
horaN =  [tritt.strip() for tritt in input().split(":")]
diaF = int(input())
horaF =  [ausgangs.strip() for ausgangs in input().split(":")]

# /*Faça os dias*/
if diaN == diaF:
	dia = diaN - diaF
elif diaN < diaF:
	dia = (diaF - diaN) - 1
else:
	dia = diaF - diaN

# /*Faça Tempo_Inicial e Tempo_Final*/

hhN = int(horaN[0])
mmN = int(horaN[1])
ssN = int(horaN[2])

hhF = int(horaF[0])
mmF = int(horaF[1])
ssF = int(horaF[2])

tempo_inicial = (hhN * 60) + mmN
tempo_final = (hhF * 60) + mmF

# /*Verifica se o tempo final é menor que o inicial*/

if tempo_final < tempo_inicial:
	tempo = 24*60 - tempo_inicial + tempo_final
	# /*Converte o tempo em horas*/
	horas = tempo / 60
	minutos = tempo % 60
else:
	tempo = tempo_final - tempo_inicial
	horas = tempo / 60
	minutos = tempo % 60

# /*Faz teste para segundos*/

if ssN < ssF:
	segundos = ssF - ssN
elif ssN == ssF:
	segundos = ssN - ssF
else:
	segundos = (60 - ssF) +ssN

print ("%d dia(s)" %dia)
print ("%d hora(s)" %horas)
print ("%d minuto(s)" %minutos)
print ("%d segundo(s)" %segundos)
