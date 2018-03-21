from random import randint
print('JOKENPÔ')
escolha = int(input('\033[1;4;30mDigite:\033[m \n\033[37m\"1\" > Pedra\033[m\n\033[30m\"2\" > Papel\033[m\n\033[34m\"3\" > Tesoura\033[m\n'))
'''1 = pedra, 2 = papel, 3 = tesoura'''
pc = randint(1, 3)
if escolha == 1 and pc == 1:
    print('A escolha do computador foi: PEDRA')
    print('\033[30mEMPATE!\033[m')
elif escolha == 1 and pc == 2:
    print('A escolha do computador foi: PAPEL')
    print('\033[31mVocê perdeu!\033[m')
elif escolha == 1 and pc == 3:
    print('A escolha do computador foi: TESOURA')
    print('\033[32mVocê venceu!\033[m')
elif escolha == 2 and pc == 2:
    print('A escolha do computador foi: PAPEL')
    print('\033[30mEMPATE!\033[m')
elif escolha == 2 and pc == 3:
    print('A escolha do computador foi: TESOURA')
    print('\033[31mVocê perdeu!\033[m')
elif escolha == 2 and pc == 1:
    print('A escolha do computador foi: PEDRA')
    print('\033[32mVocê venceu!\033[m')
elif escolha == 3 and pc == 3:
    print('A escolha do computador foi: TESOURA')
    print('\033[30mEMPATE!\033[m')
elif escolha == 3 and pc == 2:
    print('A escolha do computador foi: PAPEL')
    print('\033[32mVocê venceu!\033[m')
elif escolha == 3 and pc == 1:
    print('A escolha do computador foi: PEDRA')
    print('\033[31mVocê perdeu!\033[m')
else:
    print('WTF')
