#leia 4 nomes e sortei 1
import random
nome1 = str(input('Informe o primeiro nome: '))
nome2 = str(input('Informe o segundo nome: '))
nome3 = str(input('Informe o Terceiro nome: '))
nome4 = str(input('Informe o Quarto nome: '))
lista = [nome1 , nome2, nome3, nome4]
escolhido = random.choice(lista)
#o metodo random.choice escolhe so 1 elemnto da lista.
print('O aluno escolhido foi {}'.format(escolhido))

