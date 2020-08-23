#ler um némero entre 0-20 e mostrar ele por extenso ex: 1 - um
tupla = ('Zero','um','dois','tres', 'quatro', 'cinco', 'seis', 'sete', 'oito','nove','dez',
'onze','dose','treze','quatorze','quinze','dezesseis', 'dezessete','dezoioto','dezenove','vinte')
from time import sleep
while True: 
    numero = ' '
    while numero not in range(0,21):# Assim, o meu programa so vai aceitar números entre 0-20. 
        numero = int(input('Digite um número entre 0-20: '))
        print(f'Você digitou o número {tupla[numero]}')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Outro número: [S/N]')).strip().upper()[0]# armazena a opção s/n
    if resp == 'N':
        break
print('Finalizando...')
sleep(2)
print('Volte sempre!')
