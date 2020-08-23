#criar um jogo de advinhação que escolhe um número entre 0 e 5.
import random
from time import sleep# faz o programa espera um tempo antes de mostra a resposta.
print('-=-'*20)
print('Estou pensando em um número de 0 a 5, você consegue descobrir? ')
print('-=-'*20)
aleatorio = random.randint(0,5)#Faz o computador sortear um número.
valor = int(input('chute um numero:'))# o jogador tenta descobrir o numero pensado pelo computador.
print('Façam suas apostas ....')
sleep(2)#indica os segundos q o computador vai esperar
if (valor == aleatorio):
    print('Hora bolas, macacos me mordam, tu és um bruxão mermo em! Eu realmente pensei no número {}.'.format(aleatorio))
else:
    print('Achou errado otario! Eu pensei no número {}.'.format(aleatorio))
# a nostagia de aprender é incrivel né!