num = float(input('\033[1;30mDigite um valor numérico em Metro:\033[m '))
print('O valor de \033[4;34m{}m\033[m em centímetros é: \033[33m{}cm\033[m\nE em milímetros é: \033[31m{}mm'.format(num, (num * 100), (num * 1000)))
