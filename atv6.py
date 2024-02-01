#------Exercício: Crie uma tupla com os nomes de três frutas diferentes. Em seguida, solicite ao usuário que digite o nome de uma fruta. Verifique se a fruta digitada está presente na tupla e imprima uma mensagem correspondente.

frutas = ('maca', 'banana', 'uva')

ver = input('digite o nome de uma fruta: ')
if ver in frutas:
    print('tem na lista')
else:
    print('nao tem na lista')