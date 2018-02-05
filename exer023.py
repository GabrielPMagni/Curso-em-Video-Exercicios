num = int(input('\033[1;4;30mDigite um número até 9999:\033[m '))
u, d, c, m = num // 1 % 10, num // 10 % 10, num // 100 % 10, num // 1000 % 10
print('O número \033[31m{}\033[m tem como Unidade \033[1;33m{}\033[m, Dezena \033[1;33m{}\033[m, Centena \033[33m{}\033[m e Milhar \033[1;33m{}\033[m.'.format(num, u, d, c, m))
