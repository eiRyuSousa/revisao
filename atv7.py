#-----Exercício: Crie uma lista vazia de números. Solicite ao usuário que digite 5 números inteiros e adicione-os à lista. Em seguida, imprima a lista completa.

lista = []

for i in range(5):
    i = int(input('digite um numero: '))
    lista.append(i)
print(lista)