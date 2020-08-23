cont=0
num = int(input('Informe o número: '))
for x in range(1, num+1):
    print('{}'.format(x), end = ' ')# usando o 'end' para lateralizar o codigo ao invez de deixalo na vertical
for c in range(1 , num+1):
    if num % c == 0:
        cont += 1
print(': O número {} foi dividido {} vezes.'.format(num, cont))
if cont == 2:
    print('E é um número primo')# números primos são divisiveis por 1 e por ele mesmo. 
else:
    print('Não é um número primo')
