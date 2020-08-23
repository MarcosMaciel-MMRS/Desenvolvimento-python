#várias palavra em uma Tupla, depois mostras as palavras e cada vogais que existirem nas mesmas.
palavras = ('Aprender', 'Soldado', 'Saudade','Amizade','Doido',
            'Maluco', 'Trouxa', 'Carro', 'Moto', 'Aviao', 'Fim')
print('='*45)
print(f'{"Encontrando vogais":^45}')
print('='*45)
for palavra in palavras:
    print(f'\nNa palavra "{palavra}" tem as vogais: ', end = '')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end = ' ')
