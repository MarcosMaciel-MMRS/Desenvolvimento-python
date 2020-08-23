#Analisando condiçôes para formação de triângulos.
#condição de existência: a medida de um lado for menor q a soma dos seus outros 2 segmentos.
print('-=-'*15)
print('         ANALISADOR DE SEGMENTOS')
print('-=-'*15)
r1 = float(input('Informe o primeiro segmento de reta: '))
r2 = float(input('Informe o segundo segmento de reta: '))
r3 = float(input('Informe o terceiro segmento de reta: '))
if r1< r2+r3 and r2< r3+r1 and r3<r1+r2:
    print('É possível criar um triângulo com esses segmentos!.')
else:
    print('Não é possível criar um triângulo com esses segmentos!.')
