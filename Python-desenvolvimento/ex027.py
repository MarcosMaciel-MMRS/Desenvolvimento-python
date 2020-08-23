#mostra o nome e o ultimo nome
nome = str(input('Nome completo: ')).strip()
n = nome.split()#vai criar uma lista com o nome da pessoa fracionado
print('O seu primeiro nome é :{} '.format(n[0]))
print('O seu último nome é :{}'.format(n[len(n)-1]))
