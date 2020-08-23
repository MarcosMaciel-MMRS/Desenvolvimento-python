#ler um ano e falar se é bissexto 
#se ano % 4 == 0 é ano % 100 <> 0 ou ano % 400 == 0 <-- condição de um ano bissexto.
from datetime import date
ano = int(input('Informe o ano que quer analisar. obs: Para analisar o ano atual, digite 0: '))
if ano == 0:
    ano = date.today().year
if (ano % 4 == 0) and (ano %100 != 0) or (ano % 400 == 0):
    print('O ano {}, é Bissexto.'.format(ano))
else:
    print('O ano {}, não é bissexto.'.format(ano))
