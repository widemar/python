#Escreva um programa que solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o preço a pagar.

preco = float(input('Digite o preço: '))
percentual = float(input('Digite a porcentagem do desconto: '))

novoPreco = preco - ((preco*percentual)/100)
desconto = preco - novoPreco

print('Preço com desconto R$ %.2f, Desconto de R$ %.2f' %(novoPreco, desconto))
