import random

def jogar():

    print('-='*20)
    print('**** PEDRA, PAPEL, TESOURA *****')
    print('-='*20)

    def play():
        user = input("Qual sua escolha? 'p' para Pedra, 'a' para Papel, 't' para Tesoura\n")
        computer = random.choice(['p', 'a', 't'])

        if user == computer:
            return 'é um empate'

        if is_win(user, computer):
            return 'Você ganhou!'

        if is_win(computer, user):
            return 'Você perdeu!'

    def is_win(player, opponent):
        if (player == 'p' and opponent == 't') or (player == 't' and opponent == 'a') or (player == 'a' and opponent == 'p'):
            return True

    print(play())

if __name__ == '__main__':
    jogar()