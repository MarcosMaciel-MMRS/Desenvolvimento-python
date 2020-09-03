#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: 
#o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
#mesmo que algum dado não tenha sido informado corretamente.


#função
def ficha(nome = 'Desconhecido', gols = 0):
    print('Ficha:')
    print(f'O jogador {nome}, fez {gols} no campionato')



#programa
nome = str(input('Nome do jogador: ')).capitalize().strip()
gols = str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    g = 0
if nome.strip() == '':
    ficha(gols=gols)
else:
    ficha(nome, gols)
