#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
#já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
valores = list()
maior = menor = 0
for v in range(0,5):
    n = int(input('Digite um valor: '))
#print('Valores: {}'.format(sorted(valores))) se o exercicio permitisse estaria certo. 
#o que o comando sorted simplifica =>
    if v == 0 or n > valores[-1]:#se ele for o primeiro, ou o ultimo ja adiciona. 
        valores.append(n)
        print(f'Adcionado ao final da lista...')
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos, n)#vai adcionar na posição, o valor
                print(f'Adcionado na posição {pos} da lista')
                break
            pos +=1  
print('-='*30)  
print(f'{valores}')
print('-='*30)
