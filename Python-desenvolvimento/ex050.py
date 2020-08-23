#ler 6 números, e somar os números pares
s=0
for x in range (0,6):
    n = int(input('Informe um número: '))
    if n % 2 == 0:
        s= s+n
print('a soma dos números pares apresentados foi : {}'.format(s))
#meu programa ignora os números impares e so soma os números pares. 
