#receber um numero real e converter em inteiro
#from math import trunc
import math
n = float(input('Informe um Número Real: '))
#assim é sem importar nenhuma biblioteca
print('O número {} tem a aparte inteira {}.'.format(n, int(n)))
#print('O número {} tem a aparte inteira {}.'.format(n, math.tunc(n)))-- usando o import math(que possibilita todas as funçoes matematicas)
#print('O número {} tem a aparte inteira {}.'.format(n, trunc(n)))-- usando o from math import trunc(limitei o importe paara o trunc)
