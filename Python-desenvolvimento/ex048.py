#no intervalo de 1-500 some os numeros impares multiplos de 3. 
s=0
for x in range(0,501):
    if x % 2 != 0 and x % 3 == 0:
        s = s+x
print('soma dos números impares multiplos de 3. resultado {}'.format(s))
