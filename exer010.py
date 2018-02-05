real = float(input('\033[1;4;30mDigite um valor em R$(Reais) para ser convertido em US$(Dólar): \033[m'))
print('\033[1;32mR${:.2f}\033[m é igual a US$\033[1;34m{:.2f}\033[m -- Cotação de \033[4;33m03/Julho/2017\033[m'.format(real, (real * 3.27)))
