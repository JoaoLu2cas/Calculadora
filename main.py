import random

def play():
    user_wins = 0
    computer_wins = 0
    tie = 0
    options = ['r', 'p', 's']
    while True :
        user = input('Escolha [r]ock ,[p]aper, [s]cissors ou [e]xit: ')
        
        if user == 'e':
            print(result())
            break
        elif user not in options :
            print('Escolha r, p, s .')
            continue
        print('JO...')
        print('KEM...')
        print('PO!!!')
        computer = random.choice(options)

        if computer == user :
            print('Empate')
            print(f'O computador escolheu o mesmo que você "{computer}".')
            tie += 1
            

        elif is_win(user, computer):
            print('Você ganhou!')
            print(f'O computador escolheu "{computer}".')
            user_wins += 1
        else:
            print('Você perdeu!')
            print(f'O computador escolheu "{computer}".')

            computer_wins += 1
        continue
def is_win(player, opponent):
    if (player == 'r'and opponent =='s' or player == 'p'and opponent == 'r' \
        or player == 's' and opponent == 'p'):
        return True

def result(ganhou, empate, perdeu):
    print('\nResultado:')
    print(f'Vitórias: {ganhou}')
    print(f'Empates: {empate}')
    print(f'Derrotas: {perdeu}\n')

def main():
    play()
    

main()