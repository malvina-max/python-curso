'''
[DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um
fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele
já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule
quantos dias de vida um fumante perderá e exiba o total em dias.

'''
numecodeCigpordia = int(input('Quantos cigarros fuma por dia?'))
anosfumados = int(input('Quantos anos já fumou?'))

minutos_perdidos = numecodeCigpordia * anosfumados * 365 * 10

dias_perdidos = minutos_perdidos / (24 * 60)
print(f'voce perdera a proximadamente {dias_perdidos:.2f} dias de vida.')
