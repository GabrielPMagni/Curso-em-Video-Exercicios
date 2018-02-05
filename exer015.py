dias, km = int(input('\033[4;36mInsira o número de dias que o carro ficou alugado:\033[m ')), float(input('\033[4;36mInsira o a quantidade de quilômetros rodados:\033[m '))
print('O custo total da viagem é: \033[1;31mR${:.2f}\033[m'.format(dias * 60 + km * 0.15))
