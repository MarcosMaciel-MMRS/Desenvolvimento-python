#Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
#início, fim e passo. Seu programa tem que realizar três contagens através da função criada:                                                                                                                                  
#a) de 1 até 10, de 1 em 1
#b) de 10 até 0, de 2 em 2                                                                                                    
#c) uma contagem personalizada
from time import sleep


#função
def contador(a,b,c): # a função é responsável pela logica da contagem.
    if c == 0:
            c = 1
    if c < 0:
        c *= -1

    print(f'conatagem de {a} até {b}, pulando de {c} em {c}:')
    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont}', end = ' ', flush = True)# o flush é o que permite q ocontador gire com time
            sleep(0.5)
            cont+=c
        print('Fim!')
    else:
        cont = a
        while cont >= b:
            print(f'{cont}', end = ' ', flush = True)
            sleep(0.5)
            cont-=c
        print('Fim!')


def linha(msm):
    print('-='*30)
    print(msm.center(len(msm*3)))
    print('-='*30)


#programa
contador(1,10,1)
contador(10,0,2)
linha(msm = '   Personalizada')

a = int(input('Vai começar em quanto: '))
b = int(input('Terminar em : '))
c = int(input('Pulando de quanto em quanto: '))
contador(a, b, c)
