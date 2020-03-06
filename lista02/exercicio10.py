'''
Dados dois números inteiros positivos, determinar o máximo divisor comum entre eles
usando o algoritmo de Euclides.
'''

numero1 = int(input('Primeiro número: '))
numero2 = int(input('Segundo número: '))

if numero1 < numero2:
	numero1, numero2 = numero2, numero1

r1 = numero1 % numero2
mdc = numero2

while r1 != 0:
	r1, mdc = mdc % r1, r1

print ('O MDC de (%d,%d) é: %d' %(numero1, numero2, mdc))