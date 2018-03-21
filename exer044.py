print('\033[1;34mCondição de Pagamento\033[m')
produto = float(input('\033[1;4;30mDigite o valor do produto a ser comprado: \033[m'))
cond = int(input('\033[1;4;30mInsira a condição de pagamento:\033[m \n\033[32m\"1\" > À Vista (Dinheiro ou Cheque)\033[m\n\033[33m\"2\" > À Vista (Cartão)\033[m\n\033[32m\"3\" > 2x no Cratão\033[m\n\033[33m\"4\" > 3x ou mais no cartão\033[m\n'))
if cond == 1:
    print('Preço Final: \033[35mR${:.2f}'.format(produto - (produto * 0.1)))
elif cond == 2:
    print('Preço Final: \033[35mR${:.2f}'.format(produto - (produto * 0.05)))
elif cond == 3:
    print('Preço Final: \033[35mR${:.2f}'.format(produto))
else:
    print('Preço Final: \033[35mR${:.2f}'.format(produto +(produto * 0.2)))
