#Escreva um programa que leia três números e que imprima o maior e o menor.

n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))

if n1 < n2:
	n1, n2 = n2, n1

if n1 < n3:
	n1, n3 = n3, n1

print ('Maior: %d' %n1)

if n1 > n2:
	n1, n2 = n2, n1

if n1 > n3:
	n1, n3 = n3, n1

print ('Menor: %d' %n1)