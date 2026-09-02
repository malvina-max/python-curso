'''
Desenvolva um programa que leia uma distância em metros e mostre os valores
relativos em outras medidas.
Ex:
Digite uma distância em metros: 185.72
A distância de 185.7m corresponde a:
0.18572Km
1.8572Hm
18.572Dam
1857.2dm
18572.0cm
185720.0mm
'''
medida = float(input('Uma distancia em metros: '))
Km= medida * 0.001
Hm= medida * 0.01
Dam= medida * 0.1
dm= medida * 10
cm= medida * 100
mm= medida * 1000

print(f'A distância de {medida}metros correstonde a: \n{Km}km  \n {Hm}Hm \n {Dam}Dam \n {dm}dm \n {cm}cm \n{mm}mm')