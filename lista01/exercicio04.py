#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$ 80,00 por dia e R$ 0,25 por km rodado.

km = int(input('Digite a quantidade de km percorridos: '))
dias = int(input('Digite a quantidade de dias: '))

print ('Valor do aluguel: R$ %.2f' %(km*0.25 + dias*80))
