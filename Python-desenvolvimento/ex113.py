# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade
# da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() 
# com a mesma funcionalidade.

#função
def leiaInt(msg):
    while True:
        try:#----> Tente
            n = int(input(msg))
        except (TypeError, ValueError):# caso ocorra: 
            print('Por favor, digite um número inteiro(ex: 0,1,2,3,4...) válido.')
            continue# o comando continue garante a permanencia dentro do laço infinito
        except KeyboardInterrupt:
            print('Falta de dados por parte do usuário.')
            return 0
        else:
            return n
        


def leiaFloat(msg):
    while True:
        try: 
            n = float(input(msg))
        except (TypeError, ValueError):
            print('Por favor, digite um número inteiro válido: ex:(0.0, 1.1, 2.1, 3.2,....)')
        except KeyboardInterrupt:
            print('O usuário deixo o dado faltando, mas por padrão volta 0')
            return 0
        else:
            return n
      

#programa
n1 = leiaInt('Digite um número: ')# recebe o q foi digitado pelo usúario
n2 = leiaFloat('Digite um número Real: ')
print(f'Você digitou o número inteiro: {n1}, e o número Real: {n2}')
