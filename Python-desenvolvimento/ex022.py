#Leia um nome completo e mostre: ele maiúsculo e minúsculo, quantas letras tem(sem o espaço) e quantas letras tem o primeiro nome.
nome = str(input('Informe seu nome completo: ')).strip()# elimina os espaços antes e depois
print('Analisando o Nome {}'.format(nome.title()))# esse transforma a primeira letra de cada palavra em Maiúsculo.
print('Em maiúsculo é {}'.format(nome.upper()))
print('em minúsculo é {}'.format(nome.lower()))
print('seu nome possui {} letras.'.format(len(nome) - nome.count(' ')))# foi preciso eliminar os espaços entre as palavras.
print('seu primeiro nome tem {} letras. '.format(nome.find(' ')))# ele contou ate o primeiro espaço
