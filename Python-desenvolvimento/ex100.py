#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
#A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
#a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
numeros = list()

def sorteia(numeros):
    for n in range(0,5):
        n = randint(0,9)
        numeros.append(n)
    print(f'Os Números sorteados: {numeros}')


def somapar(numeros):
    soma = 0
    for valor in numeros:
        if valor % 2 == 0:
            soma += valor
    print(f'A some dos números pares: {soma}')
    print('FIM!')


#programa
sorteia(numeros)
somapar(numeros)
