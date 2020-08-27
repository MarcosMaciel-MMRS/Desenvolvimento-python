#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro
#e mostre uma mensagem com tamanho adaptável.      


#função
def escreva(txt):# minha função ler a mensagem que for escrita dentro do parametro escreva
    print('-' * len(txt*3))# com isso ele vai multiplicar o tamanho do que foi escrito x3 para centralizar o nome.
    print(txt.center(len(txt*3)))# o comando .center(parametro) centraliza a mensagem
    print('-'* len(txt*3))



#programa principal
texto = str(input('Escreva algo: '))
escreva(texto)# chama a função
