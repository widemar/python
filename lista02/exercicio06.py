'''
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o
valor seja inválido e continue pedindo até que o usuário informe um valor válido.
'''

nome = str(input('Digite um nome de usuário'))
senha = str(input('Digite uma senha'))

while nome == senha:
    print ('Erro')

print ('Digite o login novamente')