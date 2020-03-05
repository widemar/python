#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
#Considere que um fumante perde 10 minutos de vida a cada cigarro e calcule quantos dias de vida o fumante já perdeu. Exiba o total em dias.

qntCigarros = int(input('Quants cigarros por dia? '))
anosFumando = int(input('Anos fumando: '))

totalCigarros = (anosFumando * 365) * qntCigarros
diasPerdidos = (totalCigarros * 10)/24

print ('Dias perdidos: %d' %diasPerdidos)