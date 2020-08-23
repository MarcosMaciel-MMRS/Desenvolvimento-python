#ler 3 números e mostrar o maior valor e o menor.
a = int(input('Informe n1: '))
b = int(input('Informe n2: '))
c = int(input('Informe n3: '))
#testando condições
if (a < b) and (b< c):
    print('O maior valor foi {}, e o menor {}.'.format((c,a)))
elif (a > b) and (b > c ):
    print('O maior valor foi {}, e o menor {}.'.format(a,c)) 
elif (a == b) and (b == c):
    print('Números iguais.')
elif (a > b) and (b < c):
    print('O maior valor foi {}, e o menor {}.'.format(a,b))
else:
    print('O maior valor foi {}, e o menor {}.'.format(b,c))
