#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma 
#única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares
#e ímpares em ordem crescente.
from time import sleep
numeros = [[], []]#foi preciso criar 2 listas dentro da lista numeros, para separar os valores pares dos ímpares
valor = 0
for c in range(0,7):
    valor = int(input(f'Digite o {c+1}º valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
        print('Número Par, cadastrado com Sucesso!')
        sleep(1)
    else:
        numeros[1].append(valor)
        print('Número Ímpar, cadastrado com sucesso!')
        sleep(1)
numeros.sort()
numeros[0].sort()
numeros[1].sort()
print('-='*30)
print(f'Lista geral: {numeros}')
print(f'Lista de números pares: {numeros[1]}')
print(f'Lista de números Ímpares: {numeros[0]}')
print('-='*30)
