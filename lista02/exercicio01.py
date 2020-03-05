#Faça um Programa que peça os três lados de um triângulo. O programa deverá
# informar se os valores podem ser um triângulo. Indique, caso os lados formem um
# triângulo, se ele é: equilátero, isósceles ou escaleno.

lado1 = int(input('Lado 1: '))
lado2 = int(input('Lado 2: '))
lado3 = int(input('Lado 3: '))

'''
Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor
que a soma das medidas dos outros dois e maior que o valor absoluto da diferença entre essas medidas.
'''

if lado1 > (lado2 + lado3) or lado2 > (lado1 + lado3) or lado3 > (lado1 + lado2):
	print('Não pode ser um triângulo!')
elif lado1 == lado2 == lado3:
    # Triângulo equilátero: Todos os lados e ângulos iguais.
	print('Triângulo Equilatero')
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    #Triângulos isósceles: dois lados iguais e os ângulos opostos a esses lados iguais.
	print('Triângulo Isósceles')
else:
    #Triângulo escaleno: Todos os lados e ângulos são diferentes.
	print('Triângulo Escaleno')
