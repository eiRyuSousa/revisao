#------Exercício: Crie um dicionário com os nomes e idades de duas pessoas. Solicite ao usuário que digite o nome de uma das pessoas e imprima a idade correspondente.

dict = {'laura' : 17, 'davi': 18 }

nome = str(input('Digite um nome: '))
if nome in dict:
    print(f'{dict[nome]}')