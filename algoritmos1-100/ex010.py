'''
10) Faça um algoritmo que leia a largura e altura de uma parede, calcule e
mostre a área a ser pintada e a quantidade de tinta necessária para o serviço,
sabendo que cada litro de tinta pinta uma área de 2metros quadrados.
'''
hight = float(input('Altura da parede: '))
width = float(input('Largura da parede: '))
area = (hight * width)
print(f'Sua parede tem a dimenção de {hight} x {width} e sua área é de {area}m')
tinta = area/2
print(f'Para pintar a sua parede você precisara de {tinta} Litros de Tinta')