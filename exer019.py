from time import sleep
from random import choice
al1, al2, al3, al4 = input('\033[30mInsira o nome de um(a) aluno(a):\033[m ').strip().capitalize(), input('\033[30mInsira o nome de outro(a) aluno(a):\033[m ').strip().capitalize(), input('\033[30mInsira mais um(a) aluno(a):\033[m ').strip().capitalize(), input('\033[30mInsira o nome de mais um(a) aluno(a):\033[m ').strip().capitalize()
turma = [al1, al2, al3, al4]
sleep(1)
print('\033[42m.\033[m')
sleep(1)
print('\033[43m.\033[m')
sleep(0.5)
print('\033[41m!\033[m')
print('O(a) aluno(a) escolhido(a) é: \033[31m{}\033[m!'.format(choice(turma)))
