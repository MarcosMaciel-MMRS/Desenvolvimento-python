# ler um número inteiro e dizer se ele é primo.
# números primos são diviziveis apenas em 2 condições, por 1 ou por ele msm
num = int(input('Informe o número: '))
tot = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\033[33m', end=' ')# o end lateraliza o codigo
        tot += 1
    else:
        print('\033[3m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[m O número {}, foi divido {} vezes'.format(c, tot))
if tot == 2:
    print('E por isso ele é primo')
else:
    print('E por isso ele não é um número primo, números primos são divisiveis por 1 e por ele mesmo.')
