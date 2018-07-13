maisVelhoStr = ''       #string
maisVelhoInt = 0        #integer
media = 0.0             #float
menorDe20 = 0           #integer
contador = 0            #integer

for count in range(0, 4):
    nome = input('Digite o nome de uma pessoa: ({}/4)'.format(contador)).strip()
    idade = int(input('Digite a idade da pessoa acima: ({}/4)'.format(contador)))
    sexo = input('Digite o sexo (M/F/Outro): ({}/4)'.format(contador)).strip()

    if sexo in 'Mm' and idade > maisVelhoInt:
        maisVelhoStr = nome
        maisVelhoInt = idade
    elif sexo in 'Ff' and idade < 20:
        menorDe20 += 1
    contador += 1
    media += idade
print('-=' * 20, 'A média de idade do grupo é {} anos.\r\nO homem mais velho é {}\r\nHá {} mulheres com menos de 20 anos.'.format((media / 4), maisVelhoStr, menorDe20))
