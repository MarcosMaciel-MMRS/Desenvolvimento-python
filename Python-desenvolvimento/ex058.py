#jogo de advinhação v2.
from random import randint
computador = randint(0, 10)
print(computador)
print('Estou pensando em um número entre 0-10, será que vc consegue advinhar? ')
print('Em qual número o computador pensou? ')
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Faça sua tentativa: '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... tenta dnv ai otario!')
        elif jogador > computador:
            print('Ta em choque? calma ai meu consagrado q é menos.')
if tentativas >= 4:
    print('Porra! Burrão, mas é um burro persistente')
elif tentativas == 2 or tentativas == 3:
    print('Quase penso q é clarividência')
else:
    if tentativas == 1:
        print('Ta porra!!! ta porra!! ta porra!! Bruxão mermo em! e essa clarividência? ta de cheat?')
print('Acertou com {}palpites.'.format(tentativas))
