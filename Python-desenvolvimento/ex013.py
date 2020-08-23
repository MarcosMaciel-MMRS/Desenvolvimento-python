#escreva um codigo que calcule o reajuste de um salario em 15%
salario = float(input('Informe o seu salário: '))
nvsalario = salario+(salario * 15/100)
print('O seu salário era de R${:.2f},\n e com um reajuste de {}, passará a ser de R${:.2f}'.format(salario, '15%', nvsalario))
