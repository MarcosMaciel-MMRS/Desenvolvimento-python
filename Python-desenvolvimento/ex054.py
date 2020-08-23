#grupo de maior idade.(ler 7 anos de nascimento e separar em paior idade)
from datetime import date
anoatual = date.today().year
maioridade = 0
menoridade = 0
for x in range(0, 7):
    ano = int(input('Informe o ano de nascimento: '))
    idade = anoatual - ano
    if idade >= 18:
        maioridade += 1#armazena os maiores de idade
    else:
        menoridade += 1#armazena os menores de idade
print('Ao todo tivemos {} pessoas, maiores de idade'.format(maioridade))
print('Ao todo tivemos {} pessoas, menores de idade'.format(menoridade))
