num = int(input('\033[1;4;30mDigite um número para saber se é par ou ímpar:\033[m '))
res = num % 2
if res == 0:
    print('\033[32mO número é par.\033[m')
else:
    print('\033[34mO número é ímpar.\033[m')
