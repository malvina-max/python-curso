'''
13) Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o
seu novo salário, com 15% de aumento.
'''

sal = float(input('Digite o salario R$'))
novoSal = sal + (sal * 15/100)
print(f'O salario atual é {sal}, o novo salario com 15% de aumento será {novoSal}R$')