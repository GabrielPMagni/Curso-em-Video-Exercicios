city = input('\033[1;4;30mInsira a cidade que você nasceu:\033[m ').strip()
ct = (city[:5].lower() == 'santo')
if ct is True:
    print('\033[32mSua cidade possui \"Santo\" no início.\033[m')
else:
    print('\033[31mSua cidade não possui \"Santo\" no início.\033[m')
