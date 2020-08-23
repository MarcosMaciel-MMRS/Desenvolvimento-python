# ler 4 vezes: nome, idade e sexo. 
#a media de idade do grupo. 
#qual o nome do homem mais velho. 
#quantas mulheres tem menos de 20 anos. 
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
totalmulher20 = 0
for p in range(1, 5):
    print('------- {}ª PESSOA --------'.format(p))#contador de ficha
    nome = str(input('Nome: ')).capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('SEXO [M/F]: ')).upper()# independente do digitado sai maiúsculo. 
    somaidade += idade
    if p == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        totalmulher20 += 1
mediaidade = somaidade/4
print('A média das idades do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maioridadehomem,nomevelho))
print('O número de mulheres com menos de 20 anos: {}'.format(totalmulher20))
 