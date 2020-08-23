# nesse é pedido o dobro, triplo e o quadrado de um número.
n = int(input('Informe um número: '))
d = n*2
t = n*3
q = n** (1/2)
print('analisando {}: O dobro é {}.\n O triplo é {}. \n E a raiz quadrada é {:.2f}'.format(n, d, t, q))
# {:.2f}- significa dizer q são duas casas flutuantes, após a virgula.
#Outra forma de resolver o exercicio seria :
#n= int(input("...."))
#print('o dobro vale {}'.format(n, (n*2)))
#print('o triplo vale{},\n o quadrado vale {}'.format(n, (n*3), n, (n**(1/2))))