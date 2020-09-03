#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
#retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.


#funções
def linha():
    print('-'*30)


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - nascimento
    if idade < 16:
        print(f'Com {idade} anos, NÃO PODE VOTAR.')
    elif idade >= 16 and idade <=17 or idade >= 65:
        print(f'Com {idade} anos, o voto é opcional.')
    else:
        print(f'Com {idade} anos, o voto é obrigatório.')

#programa

linha()
while True: 
    nascimento = int(input('Em que ano voce nasceu: '))
    voto(nascimento)

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar: ')).upper().strip()[0]
    if resp == 'N':
        break
print('>>> Fim da Analise<<<')
