#ler números inteiros: somalos e apresentar quantos números foram digitados. O programa so deve parar quando digitar 999.
soma = 0
cont = 0
n = 0
while True:# o while True, cria uma loop infinito que so é interrompido, quando chega na condição que se encontra o break. 
    n = int(input('Digite um número inteiro. (999 encerrar o programa): '))
    if n == 999:
        break#interrompe o programa. 
    soma += n 
    cont +=1
print(f'Você digitou {cont} números, a soma dos mesmo é {soma}.')
