#jogo do PAR OU IMPAR, que so deve encerrar quando o usuário perder, mostrando a quantidade de vezes que ele conseguiu ganhar. 
from random import randint
from time import sleep
vitoria = derrota = cont = 0
print(''' Jogo do Par X ÍMPAR :
- O jogo consiste em 3 rodadas, assim não acontece empates. 
- O placar é mostrado no final. 
''')
while True:
    jogador = int(input('Digite um valor entre 0-10: '))
    escolha = str(input('PAR OU ÍMPAR [P/I]: ')).strip().upper()[0]#especifica que so vai usar a primeira letra
    while escolha not in 'PI':
        escolha = str(input('PAR OU ÍMPAR [P/I]: ')).strip().upper()[0]
    computador = randint(0, 10)
    resultado = jogador + computador
    print('-=-'*30)
    print(f'Você escolheu {jogador}, e o computador {computador}')
    sleep(2)
    if escolha == 'I':
        if resultado % 2 == 0:
            print('Você Perdeu! O resulatado é Par.')
            derrota += 1
            cont += 1
        if resultado % 2 != 0:
            print('Você GANHOU! O resultado é Ímpar.')
            vitoria += 1
            cont += 1
    else:
        if escolha == 'P':
            if resultado % 2 == 0:
                print('Você Ganhou! O resultado é Par.')
                vitoria += 1 
                cont += 1
            if resultado % 2 != 0:
                print('Você Perdeu! O resultado foi Ímpar.')
                derrota += 1
                cont += 1
    print('-=-'*30)
    print(f'''Placar: Vitorias: {vitoria}
        Derrotas: {derrota}''')
    if cont == 3:
        break
    if vitoria > derrota:
        print('WIN!!')
    if vitoria == derrota:
        print ('KEYED UP!')#tenso!
    else:
        print('GAME OVER!')
print('Fim do Programa.')
