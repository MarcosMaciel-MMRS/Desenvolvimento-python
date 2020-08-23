#ler varios produtos (Nome,preço). 
#A- Quantos produtos custam mais de 1000. 
#B-Qual o nome do produto mais barato. 
#C-Total gasto. 
total = cont = menor = totalmais = 0
barato = ' '
while True:
    nome = str(input('Nome do Produto: '))
    preco = float(input('Preço: '))
    cont += 1
    total += preco
    if preco > 1000:
        totalmais += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = nome
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar: [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break
print('O Total da compra foi de R${:.2f}'.format(total))
print('O numero de produtos que custa mais de R$1.000,00: {}'.format(totalmais))
print('O produto mais Barato é o {} e custa: R${:.2f}'.format(barato,menor))
