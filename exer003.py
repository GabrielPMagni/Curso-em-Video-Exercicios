num1, num2 = int(input('Diga um número: ')), int(input('Diga outro número: '))

cores = ['\033[m', '\033[1;31m', '\033[33m']
print('A soma entre {}{}{} e {}{}{} é igual a: {}{}{}.'.format(cores[2], num1, cores[0], cores[2], num2, cores[0], cores[1], (num1 + num2), cores[0]))
