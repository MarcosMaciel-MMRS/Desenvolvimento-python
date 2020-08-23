#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos
#e fechados na ordem correta.
exp = str(input('Digite sua expressão: '))
pilha = []
for simbo in exp:#obs : para uma expressão ser valida o número de parense precisa ser par. Assim, um parentese elimina outro.
    if simbo == '(':
        pilha.append('(')
    elif simbo == ')':
        if len(pilha)> 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida.')
else:
    print('Expressão inválida.')
