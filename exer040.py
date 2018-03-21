print('\033[1;36mAvaliador de Média\033[m\n')
media1 = float(input('\033[30mInsira a primeira nota do aluno: \033[m'))
media2 = float(input('\033[30mInsira a segunda nota: \033[m'))
media_final = ((media1 + media2) / 2)
if media_final < 5:
    print('\033[31mAluno Reprovado\033[m')
elif media_final >= 5 and media_final < 7:
    print('\033[33mRecuperação\033[m')
else:
    print('\033[32mAprovado\033[m')
print('\033[34mA média é: \033[m\033[30m{}\033[m'.format(media_final))
