a = 0
b = 0
def opcoes(num1, num2): #2
    try:
        opcao = int(input('Digite a opção:\n[1] Somar\n[2] Multiplicar\n[3] Maior\n[4] Novos Números\n[5] Sair do Programa\n\n>>').strip())
        if (opcao not in range(1, 6)):
            raise ValueError
        else:
            if (opcao == 1):
                somar(num1, num2)
            elif (opcao == 2):
                multiplicar(num1, num2)
            elif (opcao == 3):
                verMaior(num1, num2)
            elif (opcao == 4):
                pegarNums()
            elif (opcao == 5):
                exit()
            else:
                print('Não entendi, tente novamente')
                return opcoes(a, b)
    except TypeError:
        print('Digite somente números')
        opcoes(a, b)
    except ValueError:
        print('Digite números entre 1 e 5')
        opcoes(a, b)
    except Exception as erro:
        print('Erro inesperado: '+str(erro))
        opcoes(a, b)


def pegarNums(): #1
    def pegarNum1():
        try:
            num1 = int(input('Digite o 1º número: '))
            return num1
        except TypeError:
            print('Digite somente números')
            return pegarNum1()
        except Exception as erro:
            print('Erro inesperado: ' + str(erro))
            return pegarNum2()

    def pegarNum2():
        try:
            num2 = int(input('Digite o 2º número: '))
            return num2
        except TypeError:
            print('Digite somente números')
            return pegarNum2()
        except Exception as erro:
            print('Erro inesperado: ' + str(erro))
            return pegarNum2()

    return opcoes(pegarNum1(), pegarNum2())
 
def somar(a, b):
    try:
        print(a+b)
        opcoes(a, b)
    except Exception as erro:
        print('Erro somar()\n'+ str(erro))

def subtrair(a, b):
    try:
        print(a-b)
        opcoes(a, b)
    except Exception as erro:
        print('Erro subtrair()\n'+ str(erro))

def multiplicar(a, b):
    try:
        print(a*b)
        opcoes(a, b)
    except Exception as erro:
        print('Erro multiplicar()\n'+str(erro))

def dividir(a, b):
    try:
        print(a/b)
        opcoes(a, b)
    except Exception as erro:
        print('Erro dividir()\n'+str(erro))
def verMaior(a, b):
    try:
        if (a > b):
            print('O maior número é: '+ str(a))
            opcoes(a, b)
        elif (a < b):
            print('O maior número é: '+str(b))
            opcoes(a, b)
        else:
            print('Os números são iguais')
            opcoes(a, b)
    except Exception as erro:
        print('Erro verMaior()\n'+str(erro))

pegarNums()
