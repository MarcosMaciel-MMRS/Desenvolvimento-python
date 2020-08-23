#o programa vai ler 2 números, em seguida mostrar um menu. 
''' O programa vai pedir 2 número. 
            Tabela                 
        [1]- Soma
        [2]- Multiplica
        [3]- Maior
        [4]-Novos números
        [5]- sair
        '''
from time import sleep
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
escolha = 0
while escolha != 5:
    print('-=-'*15)
    print('''
        Tabela                 
    [1]- Soma
    [2]- Multiplica
    [3]- Maior
    [4]-Novos números
    [5]- sair
        ''')
    escolha = int(input('>>>>>>>> Qual opção: '))
    if escolha == 1:
        soma = n1+n2
        print('O resultado da soma entre {} e {} = {}'.format( n1, n2, soma))
    elif escolha == 2:
        multi = n1*n2
        print('O resultado da mutiplicação entre {} x {} = {}'.format( n1, n2, multi))
    elif escolha == 3:
        if n1 > n2:
            print('O {} é maior que {}.'.format(n1,n2))
        elif n1 == n2:
            print('Números iguais.')
        else:
            print('O {} é maior que {}.'.format(n2, n1))
    elif escolha == 4:
        n1 = int(input('Informe o primeiro número: '))
        n2 = int(input('Informe o segundo número: '))
    elif escolha == 5:
        print('FINALIZANDO....')
    else:
        print('Opção inválida. Tente novamente!')
    sleep(2)
print('Fim do Programa. Volte sempre!')
