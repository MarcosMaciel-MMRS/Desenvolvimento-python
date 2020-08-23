# Jogo DO JOKENPO
#condiçoes aninhadas
from random import randint
lista = ('pedra', 'papel', 'tesoura')
computador = randint(0,2)
print('''Sua opções são:
[ 0 ]- PEDRA
[ 1 ]- PAPEL
[ 2 ]- TESOURA''')
jogador = int(input('Informe a sua escolha: '))
print('-=-'*15)
print('O computador escolheu {}'.format(lista[computador]))
print('Sua escolha foi {}'.format(lista[jogador]))
print('-=-'*15)
if computador == 0:# pedra
  if jogador == 0:
      print('EMPATE')
  elif jogador == 1:
        print('O JOGADOR VENCEU!')
  else:
        print('O COMPUTADOR GANHOU!')
elif computador == 1:#papel
    if jogador == 0:
          print('O COMPUTADOR GANHOU!')
    elif jogador == 1:
        print('EMPATE')
    else:
        print('O JOGADOR GANHOU!')
elif computador ==2:#tesoura
    if jogador == 0:
          print('O JOGADOR GANHOU!')
    elif jogador == 1:
        print('O COMPUTADOR GANHOU')
    else:
        print('EMPATE')
