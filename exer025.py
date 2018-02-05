nome = input('\033[1;4;30mDigite seu nome completo:\033[m ').strip()
vdd = 'silva' in nome.lower()
if vdd is True:
    print('\033[32mSeu nome possui \"Silva\".\033[m')
else:
    print('\033[31mSeu nome não possui \"Silva\".\033[m')
