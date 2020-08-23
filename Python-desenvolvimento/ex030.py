#par ou ímpar
numero = int(input('Informe um número: '))
resultado = numero % 2
if resultado != 0:# se o resto da divisão por 2 for diferente de 0 é impar, e se for 0 é par
    print('O número {} é Ímpar'.format(numero))
else:
    print('O número {} é Par'.format(numero))
