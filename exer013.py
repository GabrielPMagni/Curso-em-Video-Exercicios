print('\033[1;36mCalculadora de Aumento de 15% de Salário\033[m')
print('-+-' * 15)
sal = float(input('Insira o salário: '))
print('O salário de \033[33m{:.2f}\033[m, com aumento de 15% é: \033[31m{:.2f}\033[m.'.format(sal, (sal + sal * 0.15)))
