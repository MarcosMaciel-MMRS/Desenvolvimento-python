#pegue o cateto oposto e o cateto adjacente, para mostrar o tamanho da hipotenusa de um Triângulo retângulo.
from math import hypot
co = float(input('Informe o valor do cateto oposto: '))
ca = float(input('Informe o valor do cateto adjacente: '))
x = hypot(co, ca)
#x = math.hypot(co, ca) //-- import math(modo generalizado)
#x = (ca**2+co**2) **(1/2) //-- isso é sem usar o metodo import math
print('O comprimento da hipotenusa será de {:.2f}'.format(hypot(x)))
