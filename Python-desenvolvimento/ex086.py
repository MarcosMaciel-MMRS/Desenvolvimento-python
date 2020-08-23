#Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
#No final, mostre a matriz na tela, com a formatação correta.
from random import randint
aleatorio = randint(0,10)
matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0,3):#para ler o camando na linha
    for c in range(0,3):# aqui direciona para a coluna 
        #matriz[l][c] = int(input(f'Digite um valor: ')) se eu quiser digitar valores
        matriz[l][c] = aleatorio# para test 
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'{matriz[l][c]:^6}', end = '')
    print()
