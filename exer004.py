cores = ['\033[m', '\033[1;34m', '\033[7;40m']
palavra = input('\033[1;46mDigite uma frase ou palavra:\033[m ')
print('É alfanumérico?', cores[1], palavra.isalnum(), cores[0] + '!')
print('É alfabético?', cores[1], palavra.isalpha(), cores[0] + '!')
print('É decimal?', cores[1], palavra.isdecimal(), cores[0] + '!')
print('É um número de \"1\" a \"9\":', cores[1], palavra.isdigit(), cores[0] + '!')
print('Está em minúsculo?', cores[1], palavra.islower(), cores[0] + '!')
print('É numérico?', cores[1], palavra.isnumeric(), cores[0] + '!')
print('É composta somente de espaços?', cores[1], palavra.isspace(), cores[0] + '!')
print('É capitalizada?', cores[1], palavra.istitle(), cores[0] + '!')
print('Está em caixa alta?', cores[1], palavra.isupper(), cores[0] + '!')