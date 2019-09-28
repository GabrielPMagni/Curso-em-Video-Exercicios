entendido = False
while(not entendido):
    try:
        sexo = input('Digite seu sexo: [M/F]').strip()[0]
        if (sexo not in 'MmFf'):
            print('Valores inválidos, por favor digite seu sexo: [M/F]')
        else:
            if (sexo in 'Mm'):
                print('Você selecionou sexo Masculino.')
                entendido = True
            else:
                print('Você selecionou sexo Feminino.')
                entendido = True
    except Exception as erro:
        print('What have you done?? ' + erro)
        