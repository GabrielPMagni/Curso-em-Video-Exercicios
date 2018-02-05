from random import randint
from time import sleep
pc = randint(0, 5)
print('\033[35m-=-\033[m' * 20 + '\n Vou pensar em um número de 0 a 5, tente advinhar...\n' + '\033[35m-=-\033[m' * 20)
player = int(input('\033[1;4;30mDiga o número que eu pensei:\033[m '))
if player in range(0, 6):
    pass
else:
    print('\033[4;31mNúmero inválido, assim vai errar!\033[m')
print('\033[42m  \033[m')
sleep(0.5)
print('\033[43m  \033[m')
sleep(0.5)
print('\033[41m  \033[m')
sleep(0.5)
if player == pc:
    print('\033[32mPARABÉNS! Acertou!\033[m')
else:
    print('\033[31mErrou...\033[m')
