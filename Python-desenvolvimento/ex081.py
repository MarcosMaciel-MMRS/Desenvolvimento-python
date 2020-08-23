#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
#A) Quantos números foram digitados.
#B) A lista de valores, ordenada de forma decrescente.
#C) Se o valor 5 foi digitado e está ou não na lista.
valores = list()
cont = 0
while True:# assim eu consegui capturar quantos valores o usuário quisesse
    n = int(input('Digite um número: '))
    valores.append(n)
    cont += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar: [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
valores.sort(reverse=True)# apresenta em ondem decrescente
print(f'Você digitou {cont} números para criar a lista: {valores}')
if 5 in valores:# validando se o número 5 esta presente na lista
    print('O número 5 está presente na lista.')
else:
    print('O número 5 não está presente na lista.')
