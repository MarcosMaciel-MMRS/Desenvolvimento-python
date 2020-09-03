#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from random import randint
from time import sleep
#Função
def maior():
    while True:
        n = randint(0, 9)
        print(f'Sorteando {n} valores....')
        sleep(2)
        numeros = list()
        for num in range(n):
            num = randint(0,9)
            numeros.append(num)
        print(numeros)
        if len(numeros) == 0:
            print('Não existe números para comparar!')
        else:
            print(f'O maior valor foi: {max(numeros)}')

        resp = ' '
        while resp not in 'SN':
            resp = str(input('Quer continuar: [S/N]')).upper().strip()[0]
        if resp == 'N':
            break

    print('Fim!')

#Programa
maior()
