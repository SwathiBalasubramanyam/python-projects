import random

top_range = input("Please type a number greater than 0: ")

if top_range.isdigit():
    top_range = int(top_range)
else:
    print("Please enter a number to guess")

random_num = random.randrange(1, top_range+1)
num_iter = 0

while True:
    user_input = int(input(f"Please guess a number in the range 1 {top_range} "))
    num_iter += 1
    if user_input == random_num:
        print(f"Hurray! you guessed it in {num_iter} times")
        break

    print(f"your guess is {'greater' if user_input > random_num else 'lesser'} than the actual num")

print("Game over!!")
