#Adapte o código do desafio #107, criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado.
import moeda

#Programa Principal
valor = float(input('Digite o preço:R$ '))
print(f' A aumentando 10%  de {moeda.moeda(valor)} é igual à: R${moeda.moeda(moeda.aumentar(valor))}')# isso são parametros do pacote de moedas.
print(f' Diminuindo 10%  de {moeda.moeda(valor)} é igual à: R${moeda.moeda(moeda.diminuir(valor))}')
print(f' O dobro de {moeda.moeda(valor)} é igual à: R${moeda.moeda(moeda.dobro(valor))}')
print(f' A metade de {moeda.moeda(valor)}: é R${moeda.moeda(moeda.metade(valor))}')
