import string, random

class Player:

    def __init__(self, name, deposit) -> None:
        self.name = name
        self.total_balance = deposit

    def deposit(self, amt):
        self.total_balance += amt

    def debit(self, amt):
        self.total_balance -= amt

    def can_play(self):
        return self.total_balance >= 5

class SlotMachine:

    def __init__(self) -> None:
        self.ROWS = 6
        self.COLS = 3
        self.slot_machine_grid = [["_" for i in range(3)] for i in range(6)]
        self.choices = list(string.ascii_uppercase[:6])
        self.spin_slot_machine()

    def spin_slot_machine(self):
        for col in range(self.COLS):
            col_choice = self.choices.copy()
            for row in range(self.ROWS):
                ele = random.choice(col_choice)
                col_choice.remove(ele)
                self.slot_machine_grid[row][col] = ele

    def print_slot_machine(self):
        print("*******************")
        for row in range(self.ROWS):
            print("*".join(self.slot_machine_grid[row]))
        print("*******************")

class Game:

    def __init__(self):
        input("Welcome to spin and win! Please press enter to start! ")
        self.player = Player(input("Enter your name: "), int(input("Enter the initial amnt that you would like to start with: ")))
        self.slot_machine = SlotMachine()
        self.slot_machine.print_slot_machine()
        self.play()

    def play(self):
        print("Lets start playing")
        while True:
            
            ug_row_no = int(input("Please pick a line no in range of 1-6: "))
            if ug_row_no not in range(1,7):
                print("Number not in range, pls try again.")
                continue

            ug_row_no -= 1

            self.slot_machine.spin_slot_machine()
            self.slot_machine.print_slot_machine()

            first_val = self.slot_machine.slot_machine_grid[ug_row_no][0]
            if all(map(lambda ele: ele == first_val, self.slot_machine.slot_machine_grid[ug_row_no])):
                print("Hey you just won a spin, depositing 25$ to your account!")
                self.player.deposit(25)
            else:
                print("Oh Oh, you missed it, deducting 5$ from your balance :(")
                self.player.debit(5)

            print(f"Your current balance {self.player.total_balance}")
            if not self.player.can_play():
                print("You donot have enough balance to continue playing. Ending Game.")
                break

            continue_playing = input("Do you want to continue playing y/n ?")
            if continue_playing != 'y':
                print("Withdrawing game. See you back again!")
                break

if __name__ == "__main__":
    print("Starting the game")
    game_ins = Game()
