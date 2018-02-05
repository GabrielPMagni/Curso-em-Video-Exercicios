num = float(input('\033[46mDigite um número para saber seu dobro, triplo e raíz quadrada:\033[m '))
print('O \033[32mdobro\033[m de \033[36m{}\033[m é: \033[32m{}\033[m'.format(num, (num**2)))
print('O \033[34mtriplo\033[m de \033[36m{}\033[m é: \033[34m{}\033[m'.format(num, (num**3)))
print('A \033[31mraíz quadrada\033[m de \033[36m{}\033[m é: \033[31m{}\033[m'.format(num, (num**(1/2))))
