nome = input('Insira seu nome: ').strip()
cores = ['\033[m', '\033[0;34m']

print('É um prazer, {}{}{}!'.format(cores[1], nome, cores[0]))
