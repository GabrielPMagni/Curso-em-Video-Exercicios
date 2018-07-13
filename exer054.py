from datetime import date
idadeMais, idadeMenos, contador = 0, 0, 1
hoje = date.today().year
for i in range(0, 7):
    idade = int(input('Digite o ano de nascimento de uma pessoa: ({}/7) '.format(contador)))
    contador += 1
    calc = hoje - idade
    if calc >= 0:
        if calc >= 21:
            idadeMais += 1
        else:
            idadeMenos += 1
    else:
        print('\033[33mVocê digitou uma data que ainda não chegou. Nasceu no futuro?\033[m')
print('Desses pessoas,', idadeMais, 'é(são) maior(es) de idade e', idadeMenos, 'é(são) menor(es) de idade.')
