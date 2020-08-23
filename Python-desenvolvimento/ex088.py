# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
# cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
print('-='*30)
print('             Palpites Para a Mega Sena          ')
print('-='*30)
quantidade = int(input('Informe quantos jogos você irá fazer:'))
lista = list()
jogos = list()
total = 1
while total <= quantidade:# assim eu posso criar a condição de quantidade de jogos 
    cont = 0
    while True:# aqui é a variavel que cria os numeros da lista
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()# assim a lista nao se repete
    total += 1
print('Gerando Números... ')
sleep(2)
for c in range(quantidade):
    print(f'Os números do jogo {c+1}º: {jogos[c]}')
print('-='*5,'>','Boa Sorte','<','=-'*5)
