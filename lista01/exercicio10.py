#Escreva um programa para calcular a soma de 1 a N, onde N é fornecido pelo usuário.

numeroUsuario = int(input('Escreva um número para calcular a soma de todos os antecessores: '))

cont = 1
soma = 0

while cont <= numeroUsuario:
    soma += cont
    cont += 1

print('A soma dos %i primeiros inteiros positivos é: %i' %(numeroUsuario, soma))