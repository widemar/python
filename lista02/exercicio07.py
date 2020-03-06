'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''

nome = str(input('Digite um nome de usuário'))
senha = str(input('Digite uma senha'))

while nome == senha:
    print ('Erro')
    nome = str(input('Digite o login novamente'))
    senha = str(input('Digite a senha novamente'))

print('Login cadastrado com sucesso')