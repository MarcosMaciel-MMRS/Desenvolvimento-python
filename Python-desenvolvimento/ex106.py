#Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer.
#Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
from time import sleep
#funções
cores = {'vermelho': '\033[30:41m',#global
         'verde': '\033[30:42m',
         'azul': '\033[30:44m',
         'branco': '\033[7:30m',
         'limpa': '\033[m'}


def ajuda(com):
    print(cores["branco"], end = '')
    help(com)
    print(cores["limpa"], end = '')
    sleep(2)

def titulo(msg, cor = 'limpa'):
    print('-' * len(msg * 3))
    print(msg.center(len(msg * 3)))# nao se esqueça de por parametros dentro do .center()
    print('-' * len(msg * 3))
    sleep(1)


#Programa Principal
comando = ' '
while True:
    titulo('Sistema de ajuda Pyhelp.')
    comando = str(input('FUNÇÃO OU BIBLIOTECA >'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
print('>>>Até Logo<<<')
sleep(2)
