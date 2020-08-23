#alistamento militar. 
from datetime import date
anon = int(input('Informe o ano em que você nasceu:'))
anoatual = date.today().year
idade = anoatual - anon
if idade < 18:
    saldo = 18 - idade
    print('Você Nasceu no ano de {}, possui {} anos e nao pode se alistar tente daqui há {}'.format(anon, idade, saldo ))
elif idade > 18:
    saldo = idade - 18
    print('Você Nasceu no ano de {}, possui {} anos e ja deveria ter se alistado há {} anos atrás.'.format(anon, idade, saldo))
else:
    print('É meu garato, agr tu ta fudido, levanta a bunda da cadeira e vai se alistar!')
