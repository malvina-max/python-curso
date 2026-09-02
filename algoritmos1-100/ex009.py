'''
9) Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$)
e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$3,45.
'''
Rs = float(input('Digite o Valor em real:'))
usd= (Rs*1.00)/3.45
print(f'Com {Rs}R$ você pode comprar {usd:.2f}U$')
