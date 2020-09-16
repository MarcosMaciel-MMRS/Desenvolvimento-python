# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
# um dicionário com as seguintes informações:
#– Quantidade de notas    
#– A maior nota
#– A menor nota
#– A média da turma
#– A situação (opcional)


#função
def notas(*n, sit = False):
    """[A função recebe as notas e analisa:- a quantidade, a maior nota, menor e media da turma. Além, de mostrar a situação.]

    Args:
        sit (bool, optional): [description]. Defaults to False.
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit == True:
        if r['Média'] >=7:
            r['Situação'] = 'Boa'
        elif r['Média'] >=5:
            r['Situação'] = 'Tenso'
        else:
            r['Situação'] = 'Deu RUIM!'
    print(r)


#Programa
notas(5.1, 8.2, 9.4, sit= True)
help(notas)
