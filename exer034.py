renda = float(input('\033[1;4;30mInsira o salário a ser calculado o aumento:\033[m '))
if renda > 1250:
    renda_nova = renda + renda * 0.1
else:
    renda_nova = renda + renda * 0.15
print('Com rejuste, o salário de \033[1;4;30mR${:.2f}\033[m ficará: \033[32mR${:.2f}\033[m'.format(renda, renda_nova))
