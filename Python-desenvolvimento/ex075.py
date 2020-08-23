#gerar uma tupla aleatoria com 5 números. 
#mostrar quem é o maior, e quem é o menor.
from random import randint
numeros = (randint(1,10), randint(1,10), randint(1,10),
            randint(1,10), randint(1,10)) 
print('Os números Sorteados foram: ', end = ' ')
for n in numeros:
    print(f'{n}', end = ' ')
print('\nO maior valor foi : {}'.format(max(numeros)))#metodo próprio do python que fala o maior valor de uma tupla
print('O menor valor foi: {}'.format(min(numeros)))#metodo próprio do python q mostra o menor valor
