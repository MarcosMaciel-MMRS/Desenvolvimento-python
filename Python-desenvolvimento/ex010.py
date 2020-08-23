#Cria um programa que leia o quanto vc tem de dinheiro e converta em dolar
#levando em consideração o valor do dolar == 3,27
n = float(input('Quanto de dinehiro vc possui: R$ '))
dolar = n/5.73
print('Você possui R${:.2f}. Em dolar vc teria US${:.2f}'.format(n, dolar))
