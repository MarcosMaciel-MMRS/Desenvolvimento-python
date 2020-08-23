#ler números inteiros ate mandar parar, depois mostre a média e os valores maior e menor. 
from time import sleep
resp = 'S'
soma = media = quant = maior = menor = 0
while resp in 'Ss':
    n = int(input('Informe um número: '))
    soma += n
    quant += 1
    resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
         menor = n
media= soma/quant
print('Finalizando....')   
sleep(2)
print('Você digitou {} Números. A média dos números: {}; Maior Número: {}; Menor Número: {}'.format(quant,media,maior,menor)) 
