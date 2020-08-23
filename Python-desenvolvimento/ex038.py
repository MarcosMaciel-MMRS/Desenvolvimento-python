#leia um número, e mostre quem é maior e quem é menor. 
num = int(input('Informe o primeiro número: '))
num2 = int(input('Informe o segundo número: '))
if num > num2:
    print('O número {} é maior que {}'.format(num, num2))
elif num2 > num:
    print('O número {} é maior que {}'.format(num2, num))
else:
    print('Números iguais.')
