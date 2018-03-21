print('\033[1;34mAdesão de Empréstimo Bancário para Compra Imobiliária\033[m')
print()
casa = float(input('\033[30mDigite o valor da casa a ser comprada: \033[m'))
sal = float(input('\033[30mDigite o salário do comprador: \033[m'))
anos = int(input('\033[30mNúmero de parcelas em anos: \033[m'))
mensalidade = (anos * 12) #Número de meses a ser pago
sal_percent = (sal * 0.30) #30% que não pode ser excedido na mensalidade comparado ao salário
casa_mens = (casa / mensalidade) #Preço das mensalidades da casa
if casa_mens >= sal_percent:
    print('\n\033[1;31mCrédito Negado!\nCasa não disónível para compra por ultrapassar limite de crédito.\033[m')
elif casa_mens < sal_percent:
    print('\n\033[1;32mCrédito Aprovado!\nValor da prestação: R${:.2f}\nNúmero de mensalidades: {} meses.\nMensalidade em anos: {} anos.\033[m'.format(casa_mens, mensalidade, anos))
else:
    print('\n\033[1;30;41mWTF\033[m')
