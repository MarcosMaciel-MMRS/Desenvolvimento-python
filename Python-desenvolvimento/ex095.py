#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
#do aproveitamento de cada jogador.
jogador = dict()
time = list()
geral= list()
totalg = saldo = 0
while True:# parte responsavel por receber os dados
    jogador['Nome'] = str(input('Informe o nome do jogador: '))
    jogador['jogos'] = int(input('Quantos jogos ele jogou nesse campeonato: '))
    if jogador['jogos'] != 0:
        for n in range(0, jogador["jogos"]):
            numerog = int(input(f'Quantos gols fez no {n+1}º jogo: '))
            geral.append(numerog)
            jogador['gols'] = geral[:]
            jogador['totalg'] = sum(geral)
    else:
        print('Então ele não conta')
    time.append(jogador.copy())
    geral.clear()
    #jogador.clear()# nao precisa
    #if jogador["jogos"] > 0:
    #    print(geral)
    #    print(jogador)
    #else:
    #    print(jogador)
    resp = ' '
    while resp not in 'SN':# faz parar o cadastramento
        resp = str(input('Deseja continuar: [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print('-='*40)
print('cod', end = ' ')
for i in jogador.keys():# cabeçalho da tabela
    print(f'{i:<15}', end = ' ')
print()
print('-='*40)
for k, v in enumerate(time):# parte de baixo da tabela
    print(f'{k:>4}', end = ' ')
    for d in v.values():
        print(f'{str(d):<15}', end = ' ')
    print()
print('-='*40)
while True:# parte responsavel por mostrar os dados individuais
    busca = int(input('digite o codigo para ver algum dado: '))
    if busca >= len(time):# valida a condição de busca
        print('ERRO! Jogador não encontrado')
    else:
        print(f'--- Levantamento do jogador {time[busca]["Nome"]}: ')
        print()
        for i, g in enumerate(time[busca]['gols']):# mostra os dados individual do jogador
            print(f'----- No jogo {i+1} fez {g} gols')
    print('-='*40)
    mais = ' '
    while mais not in 'SN':# condição para ver mais jogadores ou finalizar
        mais = str(input('Deseja ver outro jogador: [S/N]')).upper().strip[0]
    if mais == 'N':
        break 
print('<< Volte Sempre >>')
