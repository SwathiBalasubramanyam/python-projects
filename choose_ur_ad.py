
name = input("type your name: ")
print(f"Welcome, {name}, to this adventure!")

answer = input("you are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?").lower()

if answer == "left":
    answer = input("you have come to a river, you can walk around it or swim across.")

    if answer == "swim":
        print("you swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("you walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. you loose.")

elif answer == "right":
    answer = input("you have come to a bridge, it looks wobbly, do you want to cross it or go back.")
    print()
else:
    print("Not a valid option. You loose.")