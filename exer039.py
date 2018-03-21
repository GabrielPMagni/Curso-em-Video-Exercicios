from datetime import date
print('\033[35mQuer saber se já é para se alistar nas Forças Armadas e quanto tempo falta?\033[m')
nasc = int(input('\033[1;30mDigite seu ano de nascimento:\033[m ')) #ano de nascimento
agora = date.today().year
age = agora - nasc
print('\033[30mVocê tem \033[32m{}\033[30m anos\033[m'.format(age))
if age == 18:
    print('\033[36mDeve se alistar este ano.\033[m')
elif age > 18:
    falta = age - 18
    print('\033[36mJá deveria ter se alsiatado há \033[32m{}\033[36m anos.\033[m'.format(falta))
elif age < 18:
    falta = 18 - age
    print('\033[36mFaltam \033[32m{}\033[36m anos para se alistar.\033[m'.format(falta))
else:
    print('\033[31mWTF\033[m')
