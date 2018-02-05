r1, r2, r3 = float(input('\033[1;4;30mInsira o valor da primeira reta:\033[m ')), float(input('\033[1;4;30mInsira o valor da segunda reta:\033[m ')), float(input('\033[1;4;30mInsira o valor da terceira reta:\033[m '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[32mTais retas formam um triângulo.\033[m')
else:
    print('\033[31mTais retas não formam um triângulo.\033[m')
