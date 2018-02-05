km = float(input('\033[1;4;30mQual a distância de sua viagem?\033[m '))
if km <= 200:
    print('O preço total da viagem é: \033[32mR${:.2f}\033[m.'.format(km * 0.5))
else:
    print('O custo da viagem é: \033[32mR${:.2f}\033[m.'.format(km * 0.45))
