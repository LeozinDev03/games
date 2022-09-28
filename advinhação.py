from ast import Break
import random

def jogar():

    print("*******************************")
    print("Bem Vindo ao jogo de advinhação")
    print("*******************************")

    numero_secreto= random.randrange(1,101)
    totaltentativas = 0
    pontos = 1000

    print("Esolha seu nível de dificuldade.")
    print("(1) Fácil (2) Médio (3) Difícil (4) IMPOSSÍVEL")

    nivel =  int(input('Qual nível você escolhe?  '))

    if(nivel == 1):
        totaltentativas = 12
    elif(nivel == 2):
        totaltentativas = 7
    elif(nivel == 3):
        totaltentativas = 4
    else:
        totaltentativas = 1


    for rodada in range(1,totaltentativas + 1):
        print(f"Tentativa {rodada} de {totaltentativas}")
        chute = int(input("Digite um número entre 1 e 100: "))
        print("Voce digitou", chute)

        if(chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100!')

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto 

        if acertou:
            print("você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                    print("Você erro! O seu chute foi maior que o número secreto.")
            elif(menor):
                    print("Você errou! O seu chute foi menor do que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
    
if __name__ == '__main__':
    jogar()
