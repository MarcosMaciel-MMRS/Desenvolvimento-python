# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais,
#  informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
import moeda

#Programa Principal
valor = float(input('Digite o preço:R$ '))
print(f' A aumentando 10%  de {moeda.moeda(valor)} é igual à: {moeda.aumentar(valor, formatado=True)}')# isso são parametros do pacote de moedas.
print(f' Diminuindo 10%  de {moeda.moeda(valor)} é igual à: {moeda.diminuir(valor, True)}')
print(f' O dobro de {moeda.moeda(valor)} é igual à: R${moeda.dobro(valor, True)}')
print(f' A metade de {moeda.moeda(valor)}: é {moeda.metade(valor, True)}')
