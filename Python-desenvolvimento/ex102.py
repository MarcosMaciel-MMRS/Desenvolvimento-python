#Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o 
#número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado
#ou não na tela o processo de cálculo do fatorial.


#função
def fatorial(num, show = False):
    """
        > A função recebe um número e calcula o seu fatorial
        :num: número recebido
        :show: função para mostrar ou nao o calculo.
        :return: vai retornar o resultado do calculo
    """
    f = 1
    for c in range(num, 0, -1):
        if show == True:
            print(c, end = '')
            if c > 1:
                print(' x ', end = '')
            else: 
                print(' = ', end = '')
        f *= c
    return f


#Programa
while True:
    num = int(input('Digite um número para ver o fatorial: '))
    show = str(input('Deseja mostrar a conta: [S/N]')).upper().strip()[0]
    if show == 'S':
        print(f' {fatorial(num, show = True)}')
    else:
        print(f'Resultado: {fatorial(num)}')

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar: [S/N]')).upper().strip()[0]
    if resp == 'N':
        break
print('>>>Fim do programa<<<')
