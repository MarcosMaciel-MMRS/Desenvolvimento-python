# Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter 
# apenas os valores pares e os valores ímpares digitados, respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
valores = list()
impares = []
pares = []
while True:
    n = int(input('Digite um número: '))
    valores.append(n)
    print('Valor Adcionado com sucesso...')
    if n % 2 == 0:
        pares.append(n)
        print('Número Par adcionado..')
    else:
        impares.append(n)
        print('Número Ímpar Adcionado...')


    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar: [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
valores.sort()
impares.sort()
pares.sort()
print(f'lista completa :{valores}')
print(f'Lista de números ímpares: {impares}')
print(f'Lista de números pares: {pares}')
