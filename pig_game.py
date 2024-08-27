'''
    player1 starts the game and he/she can role the dice untill they get a 1 or if they quit. 
    If the player decides to quit then, the current score adds to the prvious score of the player
    If the player lands on 1 then, the total accumulated score becomes 0 and player looses turn.
    Player who reaches 50 points first wins
'''
import random

class Player:

    def __init__(self, name):
        self.name = name
        self.score = 0

class PigGame:

    def __init__(self):
        self.player1 = Player(input("Please type player1 name: "))
        self.player2 = Player(input("Please type player2 name: "))
        self.playing = self.player1

    def game_over(self):
        return self.player1.score >= 10 or self.player2.score >= 10

    def switch_players(self):
        if self.playing == self.player1:
            self.playing = self.player2
        else:
            self.playing = self.player1

    def play_turn(self):
        while not self.game_over():
            print(f"Rolling dice for {self.playing.name}")
            curr_score = random.randrange(1, 7)
            print(f"Dice rolled to {curr_score}")
            if curr_score == 1:
                print(f"Sorry, {self.playing.name} score is now set to 0, switching players")
                self.playing.score = 0
                self.switch_players()
            
            self.playing.score += curr_score
            print("***********************stats***************************")
            print(f"{self.player1.name} curr score is {self.player1.score}")
            print(f"{self.player2.name} curr score is {self.player2.score}")
            print("*******************************************************")

            if self.playing.score >= 10:
                break

            curr_choice = input("Do you want to continue playing? Please type y or n: ")
            if curr_choice == "n":
                self.switch_players()


    def play(self):
        self.play_turn()

        if self.player1.score >= 10:
            print(f"{self.player1.name} won!")
        else:
            print(f"{self.player2.name} won!")

game_obj = PigGame()
game_obj.play()