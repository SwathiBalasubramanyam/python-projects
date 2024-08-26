import math

print("Welcome to my python quiz!")
playing = input("Do you want to start playing the game? Please type Y or N ")
if playing.lower() != 'y':
    quit()

print("Game started")
score = 0

answer = int(input("How many planets are there in the uiverse? "))
if answer == 8:
    print("Well done! You got it correct!")
    score += 1
else:
    print("Oh no! Incorrect!")

answer = input("what does GPU stand for? ")
if answer == "graphical processing unit":
    print("Well done! You got it correct!")
    score += 1

else:
    print("Oh no! Incorrect!")

answer = input("what does ROM stand for? ")

if answer == "read only memory":
    print("Well done! You got it correct!")
    score += 1

else:
    print("Oh no! Incorrect!")

print ("You got" + str(score) + "correct!")
print (f"You got {round((score/3*100), 2)} %.")


