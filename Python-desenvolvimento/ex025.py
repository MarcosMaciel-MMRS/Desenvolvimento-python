#Leia um nome completo e veja se tem 'Silva'
nome = str(input('Informe seu nome completo: ')).strip()
print('Seu nome tem "silva"? {}'.format('silva' in nome.lower()))
