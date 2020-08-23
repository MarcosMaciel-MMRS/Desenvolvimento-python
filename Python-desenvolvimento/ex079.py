#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
#Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, 
#em ordem crescente. 
valores = list()
while True:
    n = int(input('Digite um Valor para Cadastrar: '))
    resp = ' '
    if n not in valores:
        valores.append(n)
        print('Valor Adicionado com Sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    while resp not in 'SN':
        resp = str(input('Quer cadastrar outro valor: [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Você Digitou os valores: {sorted(valores)}')
