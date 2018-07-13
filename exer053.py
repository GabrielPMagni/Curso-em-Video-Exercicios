x = True
while x is True:

    frase = input('\033[30mDigite uma frase para saber se é um \033[34mpalíndromo: \r\n\033[33m(ou digite \"?\" para saber o que é um palíndromo)\r\n\033[31m>> \"1\" para sair').strip().lower()
    zipFrase = frase.replace(' ', '')
    inverFrase = zipFrase[::-1]

    if frase == '?':
        print('Palíndromo é uma frase ou palavra que, desconsiderando espaços, pode ser lida da mesma forma. Ex: Renner.')

    elif frase == '1':
        exit()

    elif zipFrase == inverFrase:
            print('\033[30mEsta frase é um \033[34mpalíndromo!\r\n' + '=-' * 20)

    else:
        print('\033[30mEsta frase \033[31mnão\033[m \033[30mé um \033[34mpalíndromo!\r\n' + '\033[31m=-' * 20)

