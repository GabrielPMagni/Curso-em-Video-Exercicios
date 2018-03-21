num = int(input('\033[1;30mInsira um número inteiro para convertê-lo:\033[m '))
option = input('\033[30mDigite:\033[m \n\"\033[32m1\033[m\" para \033[34mBinário\033[m\n\"\033[32m2\033[m\" para \033[34mOctal\033[m\n\"\033[32m3\033[m\" para \033[34mHexadecimal\033[m\t')
if option == '1':
    print('Seu número em Binário é: \033[34m{}\033[m'.format(bin(num)[2:]))
elif option == '2':
    print('Seu número em Octal é: \033[34m{}\033[m'.format(oct(num)[2:]))
elif option == '3':
    print('Seu número em Hexadecimal é: \033[34m{}\033[m'.format(hex(num)[2:]))
else:
    print('\033[31mDígito inválido\033[m')
