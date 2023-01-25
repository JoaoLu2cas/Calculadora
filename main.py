import random

def play():
    win = 0
    lose = 0
    tie = 0
    options = ['r', 'p', 's']
    while True:
        user = input('---Escolha um das opções---\n [r]ock ,[p]aper, [s]cissors ou [e]xit: ')
        
        if user == 'e':
            print('\nResultado:')
            print(f'Vitórias: {win}')
            print(f'Empates: {tie}')
            print(f'Derrotas: {lose}\n')
            print(' Você está se desconectantando\n \
Feito por : João Luccas Marques')
            break
        elif user not in options :
            print('Escolha r, p, s .')
            continue
        print('JO...')
        print('KEM...')
        print('PO!!!')
        computer = random.choice(options)

        if computer == user :
            tie += 1
            print('Empate')
            print(f'O computador escolheu o mesmo que você "{computer}".')
            
            

        elif is_win(user, computer):
            win += 1
            print('Você ganhou!')
            print(f'O computador escolheu "{computer}".')
          
        else:
            lose += 1
            print('Você perdeu!')
            print(f'O computador escolheu "{computer}".')

        continue
def is_win(player, opponent):
    if (player == 'r'and opponent =='s' or player == 'p'and opponent == 'r' \
        or player == 's' and opponent == 'p'):
        return True

def main():
    play()
    

main()