import random

user_wins = 0
computer_wins = 0
choices = ['r', 'p', 's', 'r']

while True:
    user_ip = input("Type R/P/S or Q to quit: ").lower()
    if user_ip == "q":
        break

    if user_ip not in choices:
        continue

    computer_guess = random.choice(choices)
    
    if user_ip == 'r' and computer_guess == 's':
        print('You win!')
        user_wins += 1
    elif user_ip == 'p' and computer_guess == 'r':
        print('You win!')
        user_wins += 1
    elif user_ip == 's' and computer_guess == 'p':
        print('You win!')
        user_wins += 1
    elif user_ip == computer_guess:
        print('Its a draw!')
    else:
        print('Computer Wins!')
        computer_wins += 1

print(f"Game Over! You won {user_wins} times and lost {computer_wins}")