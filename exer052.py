x = True
while x is True:

    num = input('\033[30mDigite um valor número inteiro: (ou \"\033[33m?\033[30m\" para sair)\033[m ').strip()
    if num not in '?':
        total = 0
        if num.isnumeric():
            num = int(num)
            for loop in range(1, num + 1):
                if num % loop == 0:
                    print('\033[31m', end=' ')
                    total += 1
                else:
                    print('\033[m', end=' ')
                print('{} '.format(loop), end='')
            print('\r\n\033[mO número {} foi divisível {} vezes'.format(num, total))
            if total == 2:
                print('E por isso ele é \033[34mPRIMO\033[m')
            else:
                print('E por isso ele \033[31mNÃO É PRIMO\033[m')

            print('\r\n\r\n')

        else:
            print('Digite um número inteiro.')
    else:
        exit()
