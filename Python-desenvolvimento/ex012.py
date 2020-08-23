#calculando desconto, com 5% em em cima do produto.
produto = float(input('Informe o preço do produto: '))
novov = produto-(produto*5/100)
print('O valor do produto sem o desconto é {:.2f}, e com o desconto de {} é {:.2f} R$'.format(produto,'%5',novov))
#na segunda chave, nao coloquei limite de casas decimais pq ali é um valor estabelecido no .format "5%".
