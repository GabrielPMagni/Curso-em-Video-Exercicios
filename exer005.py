num = int(input('\033[4;35mInsira um número inteiro:\033[m '))
print('O antecessor de \033[4;35m {} \033[m número é: \033[1;31m {} \033[m!'.format(num, (num - 1)))
print('O sucessor de \033[4;35m {} \033[m número é: \033[1;31m {} \033[m!'.format(num, (num + 1)))
