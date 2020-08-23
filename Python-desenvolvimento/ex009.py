#Tabuada
n = int(input('Qual tabuada vc quer ver ? '))
print('-'*12)
for x in range(1,11):
    print('{} x {:2} = {}'.format(n, x, n*x))
print('-'*12)
#{:2} faz com que os numeros sejam lido com 2 casas 00 e assim organiza para deixar alinhado