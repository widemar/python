#Determine se um ano é bissexto.

ano = int(input('Digite um ano para saber se o mesmo é bissexto: '))

'''
Escolha que ano você quer usar. É bem fácil determinar se um ano que passou ou que vai passar ou até o atual é bissexto.
Determine se o número é divisível por 4.
Confirme que o número não é divisível por 100.
'''

if ano % 4 == 0 and ano % 100 != 0:
    print('O ano de %d é bissexto!' %ano)
else:
    print('O ano de %d não é bissexto!' %ano)
