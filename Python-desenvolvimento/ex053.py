#palíndromo, desconsiderando os espaços.
'''Identificador de palindromos:
-PALINDROMOS SÃO PALAVRAS QUE DE TRÁS PARA FRENTE É A MSM COISA
EX: APOS A SOPA
ANA
A SACADA DA CASA
ETC.. '''
frase = str(input('Informe a frase: ')).strip().lower()
palavras = frase.split()#aqui a frase foi separada em palavras
junto = ''.join(palavras)#aqui usou o comando join para juntar tudo
inverso = ''#ficou vazio pq o python é quem associa a inversão
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:#confirmação da afirmação
    print('É um palindromo')
else:
    print('Não é um palindromo, pois palindromos de tras para frente formam a msm frase.')
print('O inverso de {} é {}'.format(junto, inverso))
'''
SEM O USO DO 'FOR' ERA SO FAZER INVERSO=JUNTO[::-1]
E TERIA O MSM RESULTADO, POREM USANDO MENOS LINHAS. '''
