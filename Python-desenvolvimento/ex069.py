#Cadastro : ler idade, sexo. 
#o programa vai perguntar se o usuário deseja continuar cadastrando
#final : A- mostrar quantas pessoas tem mais de 18 anos. B- Quantas homens foram cadastrados. C- Quantas mulheres tem menos de 20 anos. 
total18 = totalH = totalm =0
while True:
    idade = int(input('Informe a idade:'))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        total18 +=1
    if sexo == 'M':
        totalH +=1
    if sexo == 'F' and idade <=20:
        totalm += 1
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resposta == 'N':
        break
print(f'Ao todo, cadastrados existem {total18} pessoas com mais de 18 anos.')
print(f'O número de Homens Cadastrados é : {totalH}')
print(f'O número de mulheres com menos de 20 anos é : {totalm}')
