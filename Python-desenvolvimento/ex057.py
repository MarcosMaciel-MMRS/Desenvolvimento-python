#validação de dados M/F 
sexo = str(input('Informe seu sexo (M/F): ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Tente novamente: ')).strip().upper[0]
print('Sexo {} salvo com sucesso.'.format(sexo))
