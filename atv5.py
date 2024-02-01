#-----Exercício: Faça um programa que solicite ao usuário que adivinhe um número entre 1 e 10. O programa deve gerar um número aleatório e verificar se o número digitado pelo usuário é igual ao número gerado. Se o número estiver correto, imprima uma mensagem de parabéns. Caso contrário, continue solicitando ao usuário que tente novamente.
import random
aleatorio = random.randint(1,10)


while True:
    num = int(input('Digite um numero entre 1 e 10: '))
    if num == aleatorio:
        print('parabens!')
    else:
        print('continue')