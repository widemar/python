#Escreva um programa que leia uma quantidade de dias, horas, minutos e segundos do usuário. Calcule o total de segundos.

dias = int(input('Quantidade de dias: '))
horas = int(input('Quantidade de horas: '))
minutos = int(input('Quantidade de minutos: '))
segundos = int(input('Quantidade de segundos: '))

segundos += minutos*60
segundos += horas*60*60
segundos += dias*24*60*60

print('O tempo total em segundos foi de: %d' %segundos)
