'''ler o valor de angulo e calculo de seno, cosseno , tangente
'''
import math
an = float(input('Digite o valor do angulo:'))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print(f'O angulo de {an} tem o seno de {seno:.2f}')
print(f'O angulo de {an} tem o cosseno de {cosseno:.2f}')
print(f'O angulo de {an} tem a tangente de {tangente:.2f}')