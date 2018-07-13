maiorPesoPessoa, menorPesoPessoa = '', ''
maiorPeso, menorPeso = 0.0, 0.0
contador = 0
for count in range(0, 5):
    nome = input('Digite o nome de uma pessoa: ').strip()
    peso = float(input('Digite o peso da pessoa acima: '))
    contador += 1
    if contador == 1:
        maiorPesoPessoa, menorPesoPessoa = nome, nome
        maiorPeso, menorPeso = peso, peso
    else:
        if peso > maiorPeso:
            maiorPesoPessoa = nome
            maiorPeso = peso
        elif peso < menorPeso:
            menorPesoPessoa = nome
            menorPeso = peso
print('A pessoa com maior peso é: {}, com {}kg\r\nE a pessoa com menor peso é: {}, com {}kg'.format(maiorPesoPessoa, maiorPeso, menorPesoPessoa, menorPeso))
