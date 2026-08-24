'''4) Desenvolva um algoritmo que leia dois números inteiros e mostre o somatório
entre eles.
Ex:
Digite um valor: 8
Digite outro valor: 5
A soma entre 8 e 5 é igual a 13.'''

n1=float(input("Digite o Primeiro Numero"))
n2=float(input("Digite o Segundo Numero"))
soma = n1 + n2 
print(" A soma de {} e {} é igual á {:.1f}".format(n1,n2,soma))