#----Exercício: Escreva uma função que receba um número como argumento e verifique se o número é par ou ímpar. A função deve imprimir uma mensagem correspondente.
def par(nmr):
    if nmr % 2==0:
        print('par')
    else:
        print('impar')

nmr = int(input('digite um numero:'))
par(nmr)

