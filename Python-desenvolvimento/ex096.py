#Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento)
#e mostre a área do terreno.

#função
def area(a, b):
    print(f'O valor do L = {a}m, e o valor de H = {b}m ')
    area = a * b
    print(f'A area desse retangulo é de: {area}m²')# para usar valores ao estilo elevado basta: alt gr + o número.

def linha():
    print('-'*30)

#Programa
a = float(input('Digite o valor de L: '))
b = float(input('Digite o valor de H: '))
linha()
area(a, b)
linha()
