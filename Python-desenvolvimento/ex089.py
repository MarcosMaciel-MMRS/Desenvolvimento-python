#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
from time import sleep
boletimgeral = list()
ficha = list()
while True:
    nome = str(input('Informe o nome: ')).capitalize()
    nota1 = float(input('Primeria Nota:'))
    nota2 = float(input('Segunda Nota: '))
    media = (nota1 + nota2)/2
    ficha.append(nome)
    ficha.append(nota1) 
    ficha.append(nota2)
    ficha.append(media)
    boletimgeral.append(ficha[:])
    ficha.clear()
    boletimgeral.sort()
    resp = ' '# essa porra faz toda a diferença............ da espaço disgraça
    while resp not in 'SN':
        resp = str(input('Deseja continuar: [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'{"Nome":<10}{"Média.":>8}')
for n in boletimgeral:
    print(f'{n[0]:<10}{n[3]:>8.1f}')
while True:
    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('Deseja olhar as notas de algum aluno: [S/N]')).strip().upper()[0]
    if opcao == 'S':
        nomep = input("Digite o nome do aluno: ").capitalize()
        for c in boletimgeral:# criei para verificar dentro de boletim se tem algum nome pesquisado
            if c[0] == nomep:# se o nome for encontrado
                print(f"Notas do aluno {c[0]}:")# retorna o nomee as notas
                print(f"NOTA 1: {c[1]:.2f}")
                print(f"NOTA 2: {c[2]:.2f}")
    else:
        break
        sleep(2)
        print('Finalizando...')
print('Volte Sempre!')
 