#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista. 
valores = list()
maior = 0
menor = 0
for c in range(0,5):
    valores.append(int(input('Digite um valor: ')))
    if c == 0:
        maior = menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]
print('-='*30)
print(f'Você digitou os valores: {valores}')
print(f'O maior valor foi: {maior}, nas posições', end = ' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ', end = '')
print(f'\nO menor valor foi: {menor}, nas posições', end = ' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}....', end = '')
#print(f"Você digitou os valores: {valores}")
#print(f"O menor valor digitado foi o {min(valores)} na posição {valores.index(min(valores))}.")
#print(f"O maior valor digitado foi o {max(valores)} na posição {valores.index(max(valores))}.")
