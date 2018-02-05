frase = input('\033[1;4;30mInsira uma frase qualquer:\033[m ').lower().strip()
contarA, firstA, lastA = frase.count('a'), frase.find('a')+1, frase.rfind('a')+1
print('A letra \"\033[31mA\033[m\" aparece \033[33m{}\033[m vezes, aparecendo a primeira vez na posição \033[33m{}\033[m e pela última vez na posição \033[33m{}\033[m.'.format(contarA, firstA, lastA))
