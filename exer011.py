print('\033[4;30mCálculo de tinta para determinada área de uma parede.\033[m')
larg, alt = float(input('\033[4mInsira a largura (Em metros quadrados):\033[m ')), float(input('\033[4mInsira a altura (Em metros quadrados):\033[m '))
print('A qunatidade de tinta necessária é: \033[1;33m{:.2f}\033[m (Litros)'.format(larg * alt / 2))
