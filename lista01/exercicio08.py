#Escreva um programa que pergunte a distância que um passageiro deseja percorrer em km.
# Calcule o preço da passagem, cobrando R$ 0,80 por km para viagens até 200 km e R$ 0,75 para viagens mais longas.

distancia = float(input('Quantos KM deseja percorrer? '))

if distancia <= 200:
    print('Preço total: %.2f' %(distancia * 0.8))
else:
    print('Preço total: %.2f' % (distancia * 0.75))