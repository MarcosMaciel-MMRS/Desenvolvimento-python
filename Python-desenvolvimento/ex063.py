#Sequência de fibonacci v1.0
#apresente os primeiros termos de uma sequência de fibonacci, de numero n
#toda sequência de fibonacci inicia por: 0 - 1 -> 0+1= 1 -> 1+1= 2 -> 2+1= 3 ->.... 
print('-='*30)
print('Sequência de fibonacci V1.0')
print('-='*30)
n = int(input('Quantos Termos você quer mostrar? '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1,t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print('-> {} '.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
    #a sacada é fazer os contadores andarem para a direita sempre substituindo os valores a serem somados. 
print('Fim')
