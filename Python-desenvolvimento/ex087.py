# Aprimore o desafio anterior, mostrando no final: 
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.
soma = soma3 = par = 0
from random import randint
aleatorio = randint(0,10)
matriz = [[0,0,0], [0,0,0], [0,0,0]]
for l in range(0,3):#para ler o camando na linha
    for c in range(0,3):# aqui direciona para a coluna 
        matriz[l][c] = int(input(f'Digite um valor: '))# se eu quiser digitar valores
        #matriz[l][c] = aleatorio# para test 
        soma += matriz[l][c]# assim cada valor adcionado sera comado ao valor anterior. 
print('-='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'{matriz[l][c]:^6}', end = '')# centraliza meu codigo dentro da matriz em 6 casas décimais. 
        if matriz[l][c] % 2 == 0:
            par += matriz[l][c]
    print()
print('-='*30)
#soma3 = ((matriz[0][2])+(matriz[1][2])+(matriz[2][2])) ----> faz a soma da terceira coluna. 
print(f'A soma de todos os valores: {soma}')
print(f'A soma dos valores pares: {par} ')
for l in range(0,3):
    soma3 += matriz[l][2]# -----> tbm armazena a soma da terceira coluna 
print(f'A soma da terceira coluna: {soma3}')
#print(f'A soma da terceira coluna: {soma3}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')
