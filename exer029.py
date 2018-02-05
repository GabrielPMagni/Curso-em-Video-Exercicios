velocidade = float(input('\033[1;4;30mQual a velocidade atual do carro?\033[m '))
if velocidade > 80:
    print('Sua multa é: R$\033[31m{:.2f}\033[m.'.format((velocidade - 80) * 7))
print('\033[4mDigija com cuidado!\033[m')
