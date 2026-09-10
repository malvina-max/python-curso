'''
A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva
um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar,
sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.

'''
dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos Km rodados? '))
pago = dias * 90 + (km * 0.20)
print('O total de a pagar é de R${:.2f}'.format(pago))