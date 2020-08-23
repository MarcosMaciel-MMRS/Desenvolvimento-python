#mostrar os 10 primeiros númeors de uma P.A, perguntando primeiro termo e a razão. 
#Melhorando o exercicio 062, perguntando se o usuário quer mostrar mais algum termo, caso seja 0, finalize. 
from time import sleep
print('Gerador de P.A  V3.0')
print('-='*15)
n = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão da P.A: '))
print('Gerando....')
sleep(2)
termo = n
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end=' ')
        termo += r
        cont += 1
    print('Pausa.')
    mais = int(input('Deseja apresentar mais quantos termos ?'))
    sleep(2)
print('FIM')
print('Foi apresentado {} P.A, começando pelo primeiro termo da P.A: {}'.format(cont-1,n))
