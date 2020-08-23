#programa que multa um veiculo acima de 80km/h( R$07,00 PARA CADA KM/H, acima do limite.)
velocidade = float(input('Informe a velocidade do veículo: '))
if velocidade >= 80:
    multa= (velocidade-80)*7# a multra vai de cada km/h acima dos 80
    print('Multado otario! vai tranquilo q se afobar entra no caixão!, mas deixa logo R${:.2f} na minha mão.'.format(multa))
else:
     print('Porra! Dirige que nem a minha avó. Pegua a reta!')
