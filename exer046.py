from time import sleep
x = 0
for esperar in range(0, 10):
    sleep(1)
    x += 1
    print('\033[30m', str(x) + '!')
print('\033[1;31mBOOOM')