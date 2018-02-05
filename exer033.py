a, b, c = float(input('\033[1;4;30mInsira o primeiro valor:\033[m ')), float(input('\033[1;4;30mInsira o segundo valor:\033[m ')), float(input('\033[1;4;30mInsira o terceiro valor:\033[m '))
menor = a
if b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c
print('O número maior é \033[31m{}\033[m\nE o menor é \033[34m{}\033[m'.format(maior, menor))
