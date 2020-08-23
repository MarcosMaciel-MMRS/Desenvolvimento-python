#ler 2 notas e falar se esta aprovado, reprovado ou de recuperação. 
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
if (nota1+nota2)/2 < 5:
    media = (nota1+nota2)/2
    print('Reprovado, sua média é de {}'.format(media))
elif (nota1+nota2)/2 > 7:
    print('Aprovado, sua média é de {}'.format(media))
else:
    print('Recuperação, sua média é de {}'.format(media))
