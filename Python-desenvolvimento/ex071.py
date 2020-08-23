#simular o funcionamento de um caixa eletrônico. No fim, mostre o valor a ser sacado 
# o programa deve mostrar a quantidade de cada cédula que serão entregues
#obs: o caixa so tem cédulas de : 50, 20 , 10 , 1. 
print('='*30)
print('{:^30}'.format('ROUBO CERTO'))
print('='*30)
valor = int(input('Quanto você deseja sacar: R$'))
total = valor
ced = 50# maior valor das cedulas
totalced = 0 # variavel que vai armazenar o número de cedulas
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0 :    
            print(f'Total de {totalced} cédulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('='*30)
print('Volte Sempre, o Banco Roubo certo agradece!')
print('Aqui você guarda seu roubo com segurança!!!')
 