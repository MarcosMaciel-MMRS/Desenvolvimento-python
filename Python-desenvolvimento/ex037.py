# rebe um número inteiro e converte ele para a opção desejada do usuário: 1- binário, 2-octal, 3-hexadecimal
num = int(input('Informe um número: '))
print('''Qual conversão você quer usar: '))
[1] Binário
[2] Octal
[3] Hexadecimal''')# com as 3 aspas, eu posso ultilizar mais linhas dentro de uma única variável.
prefe = int(input('Sua escolha: '))
if prefe == 1:
   print('O número {}, em Binário corresponde á: {}'.format(num, bin(num)[2:]))#retira a parte q indica o tipo referido e mostra so o número convertido
elif prefe == 2:
    print('O número {}, em Octal corresponde á: {}'.format(num, oct(num)[2:]))
elif prefe == 3:
    print('O número {}, em Hexadecimal corresponde á: {}'.format(num, hex(num)[2:]))
else:
    print('Opção Invalida. Tente Novamente!')
#o python converte sozinho os tipos pedidos a cima, nao foi preciso importar nenhuma biblioteca, ou aplicar fórmula. 
