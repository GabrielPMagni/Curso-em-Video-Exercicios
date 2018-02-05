from datetime import date
ano = int(input('\033[1;4;30mDigite o ano que deseja analizar (ou \"0\" para o ano atual):\033[m '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano \033[1;4;30m{}\033[m \033[32mé bissexto\033[m.'.format(ano))
else:
    print('O ano \033[1;4;30m{}\033[m \033[31mnão é bissexto\033[m.'.format(ano))
