#Faça um programa que leia 4 nomes e coloque em uma ordem aleatoria
import random # ou from random import suffle.
nome1 = str(input('Informe o nome: '))
nome2 = str(input('Informe o nome: '))
nome3 = str(input('Informe o nome: '))
nome4 = str(input('Informe o nome: '))
lista = [ nome1, nome2, nome3, nome4]
random.shuffle(lista)    #suffle(lista)//-- para 'from random import suffle'.
#shuffle significa embaralhar.
print('A ordem será {}'.format(lista))
