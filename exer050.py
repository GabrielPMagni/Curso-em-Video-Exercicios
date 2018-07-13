soma = 0
for ler in range(1, 7):
    num = float(input('Digite um número: ({}/6)'.format(ler)))
    if (num % 2) == 0:
        soma += num
    else:
        pass
print(soma)
