'''5) Faça um programa que leia as duas notas de um aluno em uma matéria e mostre
na tela a sua média na disciplina.
Ex:
Nota 1: 4.5
Nota 2: 8.5
A média entre 4.5 e 8.5 é igual a 6.5'''

nota_01 = float(input("Digite a primeira nota: "))
nota_02 = float(input("Digite a segunda nota: "))
media = int((nota_01 + nota_02)/2)
print(f"A p1 é {nota_01} e a p2 é {nota_02}, a media é: {media}")
