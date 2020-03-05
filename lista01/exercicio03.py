#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e o percentual do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input('Digite o salário: '))
percentual = float(input('Digite a porcentagem do aumento: '))

novoSalario = salario + ((salario*percentual)/100)
aumento = novoSalario - salario

print('Aumento de R$ %.2f. Novo salário R$ %.2f' %(aumento, novoSalario))
