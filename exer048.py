#soma entre números ímpares múltiplos de 3 de 1 à 500
soma = 0
for x in range(1, 501, 2):
    if (x % 3) == 0:
        soma += x
    else:
        pass
print(soma)
#20667