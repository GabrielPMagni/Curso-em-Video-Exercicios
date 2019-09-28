from random import randint
from time import sleep
def pegarNum():
    return randint(0, 10)

def jogar():
    print('Pensei num número entre 0 e 10...\nSerá que você consegue advinhar?')
    palpitesUsados = []
    num = pegarNum()
    def perguntar():
        try:
            palpite = int(input('Digite um número entre 0 e 10: '))
            if (palpite not in range(0, 11)):
                raise ValueError
            if (palpite not in palpitesUsados):
                palpitesUsados.append(palpite)
                if (palpite == num):
                    return venceu(len(palpitesUsados))
                elif (palpite > num):
                    print('Menos...')
                    return perguntar()
                else:
                    print('Mais...')
                    return perguntar()
            else:
                print('Número já usado, tente outro')
                return perguntar()
        except TypeError:
            print('Digite apenas valores numéricos, tente novamente')
            return perguntar()
        except ValueError:
            print('Digite apenas números entre 0 e 10, tente novamente')
            return perguntar()
        except Exception as erro:
            print('Erro inesperado: ' + erro)
            return perguntar()
    perguntar()

def venceu(numeroDePalpites):
    print('Parabéns! Você venceu em {} tentativas'.format(numeroDePalpites))
    sleep(5)


jogar()
