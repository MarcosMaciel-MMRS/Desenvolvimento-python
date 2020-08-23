#ler a altura e o peso, e diga o IMC da pessoa
print('-=-'*15)
print('                 Tabela IMC')
print('-=-'*15)
print('''Classifição de IMC:
-Abaixo de 18.5: Abaixo do Peso
-Entre 18.5 e 25: Peso ideal
-25 até 30: Sobrepeso
-30 até 40: Obsesidade
-Acima de 40: Obesidade Mórbida''')
altura = float(input('Informe sua Altura: '))
peso = float(input('Informe seu peso: '))
imc = peso/ (altura**2)
if imc < 18.5:
    print('Seu peso está abixo do ideal, seu IMC é de {:.2f}'.format(imc))
elif imc >=18.5 and imc< 25:
    print('seu IMC é de {:.2f}, e você esta no peso ideal'.format(imc).capitalize())#so para nao esquecer o capitalize
elif imc >=25 and imc< 30:
    print('Seu IMC é de {:.2f}, e você está acima do peso ideal.'.format(imc))
elif imc >=30 and imc <40:
    print('O seu IMC é de {:.2f}, e vc esta em Obsidade.'.format(imc))
else:
    print('Eita porra, eita porra, eita porra, GORDO PRA CARALHO, quer infartar?! Vou nem falar o IMC ')
