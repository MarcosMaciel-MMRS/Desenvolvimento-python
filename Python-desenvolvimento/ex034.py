#ler um salario e informar o valor do aumento. (Para salários maiores que R$1.250,00 aumento de 10%. Menor q isso de 15%.)
salario = float(input('Informe seu salário: '))
if salario <= 1250: 
    salario = salario+(salario*15/100)
else:
    salario = salario+(salario*10/100)
print('Com o reajuste salarial, sue novo salário será R${:.2f}.'.format(salario))
