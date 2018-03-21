from datetime import date
print('\033[1;34mCategorização da Confederação Nacional de Natação\033[m')
ano = int(input('\033[1;30mDigite a data de nascimento do atleta: \033[m'))
agora = date.today().year
idade = agora - ano
c = '\033[30mCategoria: \033[m'
if idade <= 9:
    print(c + 'Mirim')
elif idade <= 14:
    print(c + 'Infantil')
elif idade <= 19:
    print(c + 'Júnior')
elif idade >= 20:
    print(c + 'Sênior')
elif idade > 25:
    print(c + 'Master')
else:
    print('\033[31mWTF\033[m')