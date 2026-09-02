'''
12) Crie um programa que leia o preço de um produto, calcule e mostre o seu
PREÇO PROMOCIONAL, com 5% de desconto.
'''
preco = float(input('Qual é o preço do produto? R$'))
novo = preco - (preco * 5 / 100)
print(f'O produto que custava R${preco:.2f}, na promoção com desconto de 5% vai custar R${novo:.2f}')