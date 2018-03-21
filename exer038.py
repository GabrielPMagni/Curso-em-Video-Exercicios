print('\033[1;34mComparador de Números Inteiros\033[m')
num1 = int(input('\033[30mInsira o primeiro valor inteiro: \033[m'))
num2 = int(input('\033[30mInsira o segundo valor inteiro: \033[m'))
if num1 > num2:
    print('\033[36mO primeiro valor é maior.\033[m')
elif num1 < num2:
    print('\033[36mO segundo valor é maior.\033[m')
elif num1 == num2:
    print('\033[36mNão existe valor maior, os dois são iguais.\033[m')
else:
    print('\033[1;30;41mWTF\033[m')