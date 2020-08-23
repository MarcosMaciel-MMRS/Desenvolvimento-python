#forma tradicional de calcular o fatorial de um número. 
from time import sleep
from math import factorial
n = int(input('Informe o número fatorial: '))
calculo = n
fator = factorial(n)
print('Calculando {}!'.format(n))
sleep(2)
while calculo > 0: 
    print('{}'.format(calculo), end=' ')
    print(' x ' if calculo > 1 else ' = ', end=' ')
    calculo -= 1
print('''{} 
O fatorial de {} é igual à {}'''.format(fator,n,fator))
