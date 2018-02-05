num = float(input('\033[1;4;30mDiga o preço para calcular 5% de desconto:\033[m '))
print('\033[31m{:.2f}\033[m com desconto de \033[4m5%\033[m é: \033[1;35m{:.2f}\033[m'.format(num, (num - num * 0.05)))
