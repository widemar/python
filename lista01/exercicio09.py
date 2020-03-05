#Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica. Pergunte a
# quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios.
# Calcule o preço a pagar de acordo com a tabela a seguir:

#Preço por tipo e faixa de consumo
# Tipo Faixa (kWh) Preço
# Residencial Até 500 R$ 0,40
# Acima de 500 R$ 0,65
# Comercial Até 1000 R$ 0,55
# Acima de 1000 R$ 0,60
# Industrial Até 5000 R$ 0,55
# Acima de 5000 R$ 0,60

kwhConsumida = float(input('Quantidade de kWh consumida: '))
tipoInstalacao = input('Tipo de instalação (R para residências, I para indústrias e C para comércios.): ')

if tipoInstalacao == 'R' or tipoInstalacao == 'r' and kwhConsumida <= 500:
    print('Tipo de Instalação: Residencial - Valor total: %.2f' %(kwhConsumida * 0.4))
elif tipoInstalacao == 'R' or tipoInstalacao == 'r' and kwhConsumida > 500:
    print('Tipo de Instalação: Residencial - Valor total: %.2f' %(kwhConsumida * 0.65))
elif tipoInstalacao == 'C' or tipoInstalacao == 'c' and kwhConsumida <= 1000:
    print('Tipo de Instalação: Comercial - Valor total: %.2f' %(kwhConsumida * 0.55))
elif tipoInstalacao == 'C' or tipoInstalacao == 'c' and kwhConsumida > 1000:
    print('Tipo de Instalação: Comercial - Valor total: %.2f' %(kwhConsumida * 0.60))
elif tipoInstalacao == 'I' or tipoInstalacao == 'i' and kwhConsumida <= 5000:
    print('Tipo de Instalação: Industrial - Valor total: %.2f' %(kwhConsumida * 0.55))
elif tipoInstalacao == 'I' or tipoInstalacao == 'i' and kwhConsumida > 5000:
    print('Tipo de Instalação: Industrial - Valor total: %.2f' %(kwhConsumida * 0.60))
else:
    print('Digite um valor válido.')
