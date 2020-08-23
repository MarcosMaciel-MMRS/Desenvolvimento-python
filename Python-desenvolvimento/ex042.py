#formação de triângulos: equilatero, isoceles e escaleno.
#equilatero: todos os lados iguais
#isoceles: dois lados iguais
#escaleno: todos os lados diferentes
#condições aninhadas
r1 = float(input('Informe o primeiro lado: '))
r2 = float(input('Informe o segundo lado: '))
r3 = float(input('Informe o terceiro lado: '))
if r1 < r2+r3 and r2 < r1+r3 and r3 < r2+r1:
    print('Com esses segmentos de reta, é possível formar um triângulo do tipo: ')
    if r1 == r2 == r3:
        print('Equilatero')
    elif  r1 == r2 or r1 == r3 or r2 == r3:
        print('Isoceles')
    else:
        print('Escaleno')
else:
    print('Não é possível formar um triângulo com esses segmentos, tente novamente!')
