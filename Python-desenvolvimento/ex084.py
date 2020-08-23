#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.
from time import sleep
temp = list()
principal = list()
totalpessoas = maior = menor = 0
nomeM = nomem = ' '
while True:
    temp.append(str(input('Nome: ')).capitalize())
    temp.append(float(input('Peso: ')))
    totalpessoas += 1
    if len(principal) == 0:
        maior = menor = temp[1]# ao utilizar a lista temporaria vc consegue validar os maiores e menores valores. 
    else:
        if temp[1] > maior:
            maior = temp[1]
            nomeM = temp[0]
        if temp[1] < menor:
            menor = temp[1]
            nomem = temp[0]
    principal.append(temp[:])# copiando sem fazer uma ligação
    temp.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar: [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
    print('-='*30)
print(f'Lista Principal : {principal}')
print(f'Ao todo foram cadastrado(s) {totalpessoas} pessoa(s)')
print(f'As pessoas mais pesadas possuem: {maior} kg. e são: ', end = '')
for p in principal:
    if p[1] == maior:
        print(f'{p[0]}', end = ' ')
print(f'\nAs pessoas mais leves possuem: {menor} kg. e são: ', end = '')
for p in principal:
    if p[1] == menor:
        print(f'{p[0]}', end = ' ')
sleep(2)
print('\nFim do Cadastro')
