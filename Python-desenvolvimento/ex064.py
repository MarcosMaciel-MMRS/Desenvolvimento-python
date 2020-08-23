#ler numeros inteiro diferente de 999. Depois mostre quantos números foram lidos e sua soma. 
n = 0
cont = 0
nv = 0
while n != 999:
    n = int(input('Digite um número [999 para]: '))
    nv += n
    cont +=  1
print('Vodê digitou {} números e a soma desses é {}'.format(cont-1, nv-999))#famosa gambiarra. (subitrai 1 do numeros de vezes, e 999 da soma.)
