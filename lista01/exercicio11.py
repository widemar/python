#Escreva um programa quer pergunte o depósito inicial e a taxa de juros de uma poupança.
# Exiba os valores mês a mês para os primeiros 24 meses. Escreva o ganho com juros no período.

juros = float(input('Porcentagem de juros: '))
depositoInicial = float(input('Valor do depósito inicial: '))
depositoMensal = float(input('Valor do depósito mensal: '))
depositoMaisJuros = depositoInicial

contador = 1

while contador <= 24:
	depositoMaisJuros = (depositoMaisJuros + depositoMensal) + ((depositoMaisJuros + depositoMensal) * juros / 100)
	apenasJuros = depositoMaisJuros - (depositoInicial + depositoMensal * contador)
	print('% do mês: %.2f' % (contador, depositoMaisJuros))
	contador += 1

input('Seu dinheiro rendeu R$ %.2f em juros.' %(apenasJuros))