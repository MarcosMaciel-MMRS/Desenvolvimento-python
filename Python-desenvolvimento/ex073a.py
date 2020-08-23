# melhorando o codigo 073
from time import sleep
times = ('Flamengo', 'Santos', 'Palmeiras', 'Grêmio', 'Athletico-PR',
         'São Paulo', 'Internacional', 'Corinthians', 'Fortaleza', 'Goiás',
         'Bahia', 'Vasco', 'Atlético-MG', 'Fluminense', 'Botafogo', 'Ceará',
         'Cruzeiro', 'CSA', 'Chapecoense', 'Avaí')
print('Salve meu consagrado!')
sleep(1)
print('''O que você deseja ver hj? 
            Menu:
        [1] - Tabela do Brasileirão
        [2] - Os 5 primeiros
        [3] - O nome dos times em Ordem Alfabética
        [4] - Procurar time
        [5] - Os lanterninhas
        [6] - Sair de mancinho
        ''')
while True:
    opcao = str(input('Fala o q tu quer meu anjo: '))
    sleep(1)
    if opcao == '1':
        print('-='*30)
        print(f'Tabela do Brasileirao: {times}')
        print('-='*30)
    sleep(1)
    if opcao == '2':
        print('-='*30)
        print(f'Os 5 primeiros Times do Brasileirão : {times[0:5]}')
        print('-='*30)
    elif opcao == '3':
        print('-='*30)
        print(f'A Tabela do Brasileirão Em Ordem Alfabética: {sorted(times)}')
        print('-='*30)
    elif opcao == '4':
        nome = str(input('Qual o nome do time que você procura: ')).strip().capitalize()
        print('-='*30)
        print('O time que você procura se encontra na : {}ª Posição.'.format(times.index(nome)+1))
        print('-='*30)
    elif opcao == '5':
        print('-='*30)
        print(f'Os Lanterninhas São : {times[16:]}')
        print('-='*30)        
    outraopcao = ' '
    while outraopcao not in 'SN':
        outraopcao = str(input('Deseja outra coisa: [S/N]')).strip().upper()[0]
        if outraopcao == 'N':
            break
    if opcao == '6':
        break
sleep(2)
print('Já vai Tarde Irmão! Mas se quiser brotar dnv TMJ!!!')
