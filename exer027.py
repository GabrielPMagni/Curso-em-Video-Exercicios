nome = input('\033[1;4;30mInsira seu nome completo:\033[m ').strip()
sep_nome = nome.split()
print('\033[35mPrazer!\033[m\nSeu primeiro nome é \033[32m{}\033[m, e seu último sobrenome é \033[32m{}\033[m.'.format(sep_nome[0], sep_nome[-1]))
