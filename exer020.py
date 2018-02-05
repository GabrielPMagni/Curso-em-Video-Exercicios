from random import shuffle
from time import sleep
print('\033[1;4;30mDigite o nome dos alunos após cada número:\033[m')
al1, al2, al3, al4 = input('1: ').strip().capitalize(), input('2: ').strip().capitalize(), input('3: ').strip().capitalize(), input('4: ').strip().capitalize()
turma = [al1, al2, al3, al4]
shuffle(turma)
print('\033[42m  \033[m')
sleep(1)
print('\033[43m  \033[m')
sleep(1)
print('\033[41m  \033[m')
print('A ordem de apresentação é: \033[1;4;31m{}\033[m!'.format(turma))
