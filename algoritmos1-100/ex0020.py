'''
lista com ordem das pessoas que vão apresentar o trabalho
'''
import random
n1 = str(input('primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)