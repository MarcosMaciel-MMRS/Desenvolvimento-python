#custo de uma viagem. ate 200km( R$0,50), mais q isso (R$0,45)
distancia = float(input('Informe a distância: '))
print('Por essa distância {}km: '.format(distancia))
if distancia <= 200: 
    preco = distancia * 0.50
    print('O valor da passagem será de R${:.2f}.'.format(preco))
else:
    preco = distancia * 0.45
    print('O valor da passagem será de R${:.2f}.'.format(preco))
