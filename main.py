import random
user_wins = 0
bot_wins = 0

escolhas = ['pedra', 'papel', 'tesoura']
print('Seja bem-vindo ao Jokempô')

def enter():
    while True:
        mode = input(('Escolha [r]pedra [p]papel ou [s]tesoura: ')).lower()
        if mode in 'r rock p paper s scissors'.split():
            return mode
        else :
            print('Escolha r,p ou s')
            
def options():
    random_choice = random.choices(escolhas)
    if random_choice == 'pedra' and enter() == 's':
        print('você ganhou')
        user_wins += 1
    elif random_choice == 'papel' and enter() == 'r':
        print('você ganhou')
        user_wins += 1
    elif random_choice == 'tesoura' and enter() == 'p' :
        print('você ganhou')
        user_wins += 1
    else:
        print('Você perdeu')
        bot_wins += 1

def main():
    enter()
    options()
main()