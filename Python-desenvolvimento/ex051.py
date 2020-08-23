#Progressão Aritmética, os 10 primeiros termos
n = int(input('Primeiro termo: '))
r = int(input('Informe a razão: '))
decimo = n + (10-1) * r
for x in range (n, decimo + r, r):
    print('{}'.format(x), end= '-> ')
print('Acaboum')
