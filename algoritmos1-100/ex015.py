'''
15) Crie um programa que leia o número de dias trabalhados em um mês e mostre o
salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25
por hora trabalhada.

'''
dias = int(input('Digite os dias trabalhados: '))
salPordia = (8 * 25)
salario = dias * salPordia
print('Sabendo que o funcionario trabalhou {}dias, o seu salario será R${:.2f} '.format(dias,salario))