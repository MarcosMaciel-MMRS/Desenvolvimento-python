#gerenciador de compres
''' condições de compra:
-À vista dinheiro/cheque: 10% de desconto
-À vista no Cartão: 5% de desconto
-Em até 2x no cartão: preço normal
-3x ou mais no cartão: 20% de JUROS'''
print('-=-'*15)
print('          Gerenciador de vendas')
print('-=-'*15)
preco = float(input('Informe o valor do produto:'))
pagamento = int(input('''formas de pagamento:
[1]-À VISTA DINHEIRO/CHEQUE
[2]-À VISTA NO CARTÃO
[3]-EM ATÉ 2X NO CARTÃO 
[4]-3X OU MAIS NO CARTÃO
Selecione sua forma de pagamento: '''))
if pagamento == 1:
    desconto = preco - (preco*10/100)
    print('O preço custa R${:.2f}, e com a forma de pagamento irá para R${:.2f}'.format(preco, desconto))
elif pagamento == 2:
    desconto = preco - (preco*5/100)
    print('O preço custa R${:.2f}, e com a forma de pagamento irá para R${:.2f}'.format(preco, desconto))
elif pagamento == 3:
    desconto = preco/2
    print('O valor do produto é de R${:.2f}, e o valor das parcelas para 2x fica de R${:.2f}.'.format(preco, desconto))
else:
    parcelas = int(input('Informe o número de parcelas: '))
    precon = preco + (preco*20/100)
    desconto = precon/parcelas
    print('O valor do produto é de R${:.2f}, e parcelado para {}x custará R${:.2f} COM JUROS.'.format(preco, parcelas ,desconto))
