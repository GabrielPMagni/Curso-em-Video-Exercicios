print('\033[1;34mCalculadora de IMC\033[m\n-=-=-=-=-=-=-=-=-=-=-')
peso = float(input('\033[30mInsira seu peso em kilogramas: '))
altura = int(input('Digite sua altura em centímetros: \033[m'))
imc = (peso / ((altura / 100) ** 2))
print('O seu IMC é: \033[1;30;47m{:.1f}\033[m'.format(imc))
if imc < 16:
    print('\033[31mMuito abaixo do peso ideal\033[m')
elif imc < 18.5:
    print('\033[33mAbaixo do peso ideal\033[m')
elif imc < 25:
    print('\033[32mPeso ideal\033[m')
elif imc < 30:
    print('\033[33mSobrepeso\033[m')
else:
    print('\033[31mObesidade mórbida\033[m')
