#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 
#a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
#Ex: n = leiaInt(‘Digite um n: ‘)

#Função
def leiaInt(txt):# a função válida se é um número ou n
    ok = False# começa sendo falso e so para quando for verdadeiro
    valor = 0
    while True:
        n = str(input(txt))
        if n.isnumeric():# se for um número o valor consegue ser retornado
            valor = int(n)
            ok = True
        else:
            print(f'\033[0;31mERRO! Digite um número válido.\033[m')
        if ok == True:
            break
    return valor# retorna o valor
#Porgrama
n = leiaInt('Digite um número: ')# recebe o q foi digitado pelo usúario
print(f'Você digitou o número: {n}')
