#ler um nome de uma cidade e verificar se começa com 'SANTO'
cidade1 = str(input('Informe o nome de uma Cidade: ')).strip()
primeiron = (cidade1[0:5].capitalize())
print(primeiron)
if (primeiron =='Santo'):
    print('Verdadeiro')
else:
    print('Falso')