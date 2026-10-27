'''

'''
frase = 'curso em video de python'
'''
#fatiamento
print(frase[9])
print(frase[9:13]) #pegar de 9 até 13
print(frase[9:21]) #pegar de 9 até 21
print(frase[9:21:2]) #pegar de 9 até 21 pulando de 2 em 2
print(frase[:5]) #começa do inicio e vai até o 5
print(frase[15:]) #começa do 15 ate ao final
print(frase[9::3]) #começa do 9 e vai a te ao final pulando de 3 em 3

#análise

print(len(frase))  #cumprimento da frase
print(frase.count('o')) #contar quantas vezes aparece o 'o'
print(frase.count('o')) #contar quantas vezes aparece o 'o'
print(frase.count('o',0,13)) #contar quantas vezes aparece o 'o' até o elemento 13
print(frase.find('deo')) #encontre o 'deo' se não encontrar aparece -1
print('curso' in frase)

#Transformação

print(frase.replace('video','Android')) #substituir a primeira palavra pela segunda
print(frase.upper()) #transformar em maiusculo
print(frase.lower()) #transformar em minusculo
print(frase.capitalize()) #captalizar
print(frase.title()) #analisar quantas palavras tem na frase
print(frase.strip())
'''
#divisão de string

print(frase.split()) #dividir a string em lista
print('-'.join(frase)) #fazer junção