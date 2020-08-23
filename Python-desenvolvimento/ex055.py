#maior e menor peso lido de 5 pessoas
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('Informe o peso: ').format(p))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi de {}kg'.format(maior))
print('O menor peso foi de {}kg'.format(menor))
