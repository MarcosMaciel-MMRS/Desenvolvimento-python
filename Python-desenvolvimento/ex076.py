#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
#na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
Tabela = ('Lapís', 1.75,
        'Borracha', 2,
        'Caderno', 15.90,
        'Estojo', 25,
        'Transferidor', 4.20,
        'Compasso', 9.99,
        'Mochila', 120.32,
        'Canetas', 22.30,
        'Livro', 34.90)
print('='*45)
print(f'{"TABELA DE PREÇOS":^40}')
print('='*45)
for pos in range(0,len(Tabela)):
    if pos % 2 == 0:
        print(f'{Tabela[pos]:.<30}', end = ' ')#< centraliza a esquerda o texto
    if pos % 2 == 1:
        print(f'R${Tabela[pos]:>7.2f}')#.2f e para formatar como dinheiro. / > centraliza na direita o texto. 
