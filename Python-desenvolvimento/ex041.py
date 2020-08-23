print('''CLASSIFICAÇÃO:
Até 9 anos: MIRIM
Até 14 anos: INFANTIL
Até 19 anos: JUINIOR
Até 25 anos: Sênior
Acima: Master''')
idade = int(input('Informe sua idade: '))
if idade <=0:
    print('Invalido, não é possível classificar!')
if idade>0 and idade<= 9:
    print('Classificação: MIRIM')
elif idade > 9 and idade<=14: 
    print('Classificação: INFANTIL')
elif idade >14 and idade<=19:
    print('Classificação: JUNIOR')
elif idade >19 and idade <=25:
    print('Classificação: Sênior')
elif idade >25:
    print('Classificação: Master')
