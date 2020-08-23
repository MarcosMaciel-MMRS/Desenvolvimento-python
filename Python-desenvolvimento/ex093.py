#Crie um programa que gerencie o aproveitamento de um jogador de futebol.
#O programa vai ler o nome do jogador e quantas partidas ele jogou.
#Depois vai ler a quantidade de gols feitos em cada partida. No final,
#tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = dict()
geral = list()
totalg = saldo = 0
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
#if jogador["jogos"] > 0:
#    print(geral)
#    print(jogador)
#else:
#    print(jogador)
for k, v in jogador.items():
    print(f'{k}: {v}')
print('Fim do Cadastro')
