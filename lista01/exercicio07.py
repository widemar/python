#Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. Para salários superiores a R$ 2.250,00,
# calcule um aumento de 10%. Para os valores inferiores ou iguais, de 15%.

salario = float(input('Digite o salário: '))

if salario > 2250:
    print('Salário total: %.2f' %(salario + ((salario * 0.1) / 100)))
else:
    print('Salário total: %.2f' % (salario + ((salario * 0.15) / 100)))
