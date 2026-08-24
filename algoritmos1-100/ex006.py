'''6) Faça um programa que leia um número inteiro e mostre o seu antecessor e seu
sucessor.
Ex:
Digite um número: 9
O antecessor de 9 é 8
O sucessor de 9 é 10'''
n1=int(input("Digite um numero inteiro"))
antecessor =(n1 - 1)
sucessor = (n1 + 1)
print(f"numero é {n1}, sucessor é {sucessor} o antecessor{antecessor}")
