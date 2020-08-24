#Crie um programa que leia nome, sexo e idade de várias pessoas,
#guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
#No final, mostre: 
#A) Quantas pessoas foram cadastradas 
#B) A média de idade 
#C) Uma lista com as mulheres 
#D) Uma lista de pessoas com idade acima da média
from time import sleep
dados = dict()
geral = list()
totalp = mediai = 0
while True:#parte responsavel por receber os dados e categorizar. reposicionando para cada local
    dados['nome'] = str(input("Nome: ").capitalize())
    dados['sexo'] = ' '
    while dados['sexo'] not in 'MF':# validador de informações
        dados['sexo'] = str(input("sexo: [M/F]").upper().strip()[0])
        if dados['sexo'] not in 'MF':
            sleep(1)
            print('ERRO! Responda apenas com M ou F.')
    dados['idade'] = int(input("Idade: "))
    mediai += dados['idade']
    geral.append(dados.copy())
    totalp += 1
    dados.clear()

    resp = ' '
    while resp not in 'SN':# responsavel por finalizar o programa
        resp = str(input('Deseja continuar: [S/N]').upper().strip()[0])
        if resp not in 'SN':
            sleep(1)
            print('ERRO! Responda apenas com S OU N.')
    if resp == 'N':
        break
print('-='*30)
print(f'A) O número de pessoas cadastradas: {totalp}')
print(f'B) Média das idades: {mediai/totalp} anos.')
print(f'C) Lista com as mulheres cadastradas: ', end = '')
print()
for p in geral:# a variavel verifica dentro da lista[cada dicionario], e analisa a posição "sexo".
    if p['sexo'] == 'F':# se for do sexo feminino ele retorna o nome.
        print(p['nome'])
print(f'D) Uma lista das pessoas acima da média das idades: ', end = '')
print()
for p in geral:# essa variavel verifica se alguem possui mais idade que a média.
    if p['idade'] > mediai/totalp:# observe q o p, indica o dicionario, assim da para usar o metodo p.items()
        #print(f'{p["nome"]} com idade {p["idade"]}')
        print()
        for k, v in p.items():# assim ele vai mostrar os dados das pessoas com idade acima da media
            print(f'{k} = {v}', end = ' ')# chave = valor
        print()
sleep(1)
print('>> Fim do Cadastro! <<')
