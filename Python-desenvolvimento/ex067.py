#O programa deve perguntar qual tabuada o usuário quer ver, e o programa so encerra quando o número for negativo. 
from time import sleep
while True:
    tabuada = int(input('Qual Tabuada você deseja ver? '))
    sleep(2)
    if tabuada < 0:
        break
    print('-'*30)
    for c in range(1,11):
        print(f'{tabuada} X {c} = {tabuada * c}')# usando esse print acaba ficando mais pratico, e simple o código.
    print('-'*30)
print('Programa encerrado. Volte sempre!')
