#------Exercício: Escreva um programa que solicite ao usuário que digite um número inteiro. Verifique se o número é positivo, negativo ou igual a zero, e imprima uma mensagem correspondente.

num = int(input('digite um numero: '))

if num > 0:
    print('numero positivo')
elif num < 0:
    print('numero negativo')
elif num == 0:
    print('numero igual a zero')