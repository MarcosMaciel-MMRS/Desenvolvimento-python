#leia um ângulo e mostre o seno, cosseno e a tangente
import math
#from math import radians, sin, cos, tan //-- fazendo isso seria preciso tirar os referenciamentos ex: seno = sin(radians(angu))
angu = float(input('Digite um angulo: '))
seno = math.sin(math.radians(angu))
coss = math.cos(math.radians(angu))
tang = math.tan(math.radians(angu))
print('O ângulo {}, tem como Seno {:.2f}'.format(angu, seno))
print('O ângulo {}, tem como Coss {:.2f}'.format(angu, coss))
print('O ângulo {}, tem como Tang {:.2f}'.format(angu, tang))

