#resposta do guanabara
tupla = ('Zero','um','dois','tres', 'quatro', 'cinco', 'seis', 'sete', 'oito','nove','dez',
'onze','dose','treze','quatorze','quinze','dezesseis', 'dezessete','dezoioto','dezenove','vinte')
while True:
    num = int(input('Digite um número entre 0-20: '))
    if 0 <= num <=20:
        break
    print('Tente novamente.', end = ' ')
print(f'Você digitou o número {tupla[num]}')
