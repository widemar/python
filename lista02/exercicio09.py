'''
A sequência de Fibonacci é a seguinte: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Sua regra de formação
é simples: os dois primeiros elementos são 1; a partir de então, cada elemento é a soma dos
dois anteriores. Faça um algoritmo que leia um número inteiro calcule o seu número de
Fibonacci. F1 = 1, F2 = 1, F3 = 2, etc.
'''

fibonacci = [1, 1]
i = 0
numero = int(input("digite número: "))

while numero > len(fibonacci):
    fibonacci.append(fibonacci[i] + fibonacci[i+1])
    i+=1

print ('Fibonacci(%d): %d'% (numero, fibonacci[numero-1]))