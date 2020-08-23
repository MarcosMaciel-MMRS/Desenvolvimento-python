print('Gerador de P.A')
print('-='*15)
n = int(input('Informe o primeiro termo: '))
r = int(input('Informe a razão da P.A: '))
termo = n
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end=' ')
    termo += r
    cont += 1
print('Fim')
