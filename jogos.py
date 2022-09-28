import forca
import advinhação
import Jokenpô

def escolhe_jogo():
    print("*******************************")
    print("***** Escolha seu jogo! ********* ")
    print("*******************************")

    print('(1) forca (2) Advinhação (3) Jokenpô ')

    jogo = int(input('Qual jogo você escolhe? '))

    if jogo == 1:
        print('jogando forca')
        forca.jogar()

    elif jogo == 2:
        print('Jogando advinhação')
        advinhação.jogar()

    else:
        print('jogando Jokenpô')
        Jokenpô.jogar()

if __name__ == '__main__':
    escolhe_jogo()