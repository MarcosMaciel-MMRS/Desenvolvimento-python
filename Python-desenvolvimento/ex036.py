#empréstimos bancários. pegue o valor da casa, o salario da pessoa e em quanto tempo ela quer pagar. 
#se as parcelas ficarem acima de 30% do salario, negue o imprestimo. 
casa = float(input('Informe o valor da casa: R$'))
salario = float(input('informe seu salario: R$'))
tempo = int(input('Em quanto tempo planeja pagar: '))
parcela = casa/(tempo*12)#para fazer a conta com base em anos, levando em conta as parcelas mensais.
print('Para pagar um casa de R${:.2f} e em {}anos, suas parcelas ficariam de R${:.2f}'.format(casa, tempo, parcela))
if parcela >= (salario*30/100):
    print('Com seu salário atual, não é possível efetuar esse empréstimo.')
else:
    print('Empréstimo aprovado')
