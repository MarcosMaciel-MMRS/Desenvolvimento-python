#simular o funcionamento de um caixa eletrônico. No fim, mostre o valor a ser sacado 
# o programa deve mostrar a quantidade de cada cédula que serão entregues
#obs: o caixa so tem cédulas de : 50, 20 , 10 , 1. 
#tentei da um up grade
from time import sleep
print('='*45)
print('{:^45}'.format('Bem vindo ao Banco Roubo Certo!'))
print('='*45)
print('''
OPÇÕES :
Emprestimo SAQUE - [ 1 ]
Deposito - [ 2 ] 
EXTRATO - [ 3 ]
Nova Operação - [ 4 ]
Sair - [ 5 ] ''')# ainda nao pensei no que fazer com a operação numero 4.  
deposito = 0
opcao = ' '
while opcao not in '5' :
    opcao = str(input('Informe a opção: '))
    if opcao == '1':
        valor = int(input('Informe o valor de Emprestimo Saque: R$'))
        total = valor
        ced = 50
        totced = 0
        while True:
            if total >= ced:
                total -= ced
                totced += 1
            else:
                if totced > 0:
                    print(f'Todal de {totced} Cédulas de {ced}')
                if ced == 50:
                    ced = 20
                elif ced == 20:
                    ced = 10
                elif ced == 10:
                    ced = 1
                totced = 0# aqui ele volta o numero de cedulas para 0, toda vez q ele muda de casa(ou seja, quando muda a casa decimal. )
                if total == 0:
                    break
    else:
        if opcao == '2':
            valord = int(input('Deposito de: R$'))
            deposito = valord
            sleep(2)
            print('Seu Deposito foi Realizado com sucesso!')
        if opcao == '3':
            print('Puxando Saldo....')
            sleep(2)
            print('Na sua conta tem: R${}'.format(deposito))
        if opcao == '5':
            print('Fim da  Operação. Finalizando....') 
            sleep(2)
            break
print('Volte sempre! O Banco Roubo Certo Agradece!')
# da para tomar o exercicio 59 como base. 
