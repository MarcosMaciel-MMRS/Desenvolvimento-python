#um programa que leia quantos 'A' APRECEM,  a primeira posição e a ultima q aparece o 'A'
frase = str(input('digite uma frase: ')).upper()
print('A letra A apareceu {} vezes na frase'.format(frase.count('A')))
print('E apareceu A primeira vez na posição {}'.format(frase.find('A')+1))
print('E apareceu A ultima vez na posição {}'.format(frase.rfind('A')+1))
