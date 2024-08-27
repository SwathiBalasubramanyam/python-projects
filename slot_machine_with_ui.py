import string
import random
import tkinter as tk
from tkinter import messagebox

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
        self.slot_machine_grid = [["_" for _ in range(3)] for _ in range(6)]
        self.choices = list(string.ascii_uppercase[:6])
        self.spin_slot_machine()

    def spin_slot_machine(self):
        for col in range(self.COLS):
            col_choice = self.choices.copy()
            for row in range(self.ROWS):
                ele = random.choice(col_choice)
                col_choice.remove(ele)
                self.slot_machine_grid[row][col] = ele

class Game:

    def __init__(self, root):
        self.root = root
        self.root.title("Slot Machine Game")
        self.player = None
        self.slot_machine = SlotMachine()

        # Setup UI elements
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.root, text="Welcome to Spin and Win!", font=("Helvetica", 16)).pack(pady=10)
        tk.Label(self.root, text="Enter your name:").pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        tk.Label(self.root, text="Enter initial deposit:").pack()
        self.deposit_entry = tk.Entry(self.root)
        self.deposit_entry.pack()

        tk.Button(self.root, text="Start Game", command=self.start_game).pack(pady=10)

        self.slot_machine_frame = tk.Frame(self.root)
        self.slot_machine_frame.pack(pady=10)

        self.balance_label = tk.Label(self.root, text="Balance: $0", font=("Helvetica", 14))
        self.balance_label.pack(pady=5)

        tk.Label(self.root, text="Pick a line number (1-6):").pack()
        self.line_entry = tk.Entry(self.root)
        self.line_entry.pack()

        tk.Button(self.root, text="Spin", command=self.play).pack(pady=10)

    def start_game(self):
        if not self.name_entry.get():
            messagebox.showerror("Error", "You need enter name to start the game!")
            return
        if not self.deposit_entry.get():
            messagebox.showerror("Error", "You need enter initial deposit to start the game!")
            return

        name = self.name_entry.get()
        deposit = int(self.deposit_entry.get())

        if name and deposit:
            self.player = Player(name, deposit)
            self.update_balance_label()
            self.draw_slot_machine()

    def draw_slot_machine(self):
        for widget in self.slot_machine_frame.winfo_children():
            widget.destroy()

        for row in range(self.slot_machine.ROWS):
            row_frame = tk.Frame(self.slot_machine_frame)
            row_frame.pack()
            for col in range(self.slot_machine.COLS):
                label = tk.Label(row_frame, text=self.slot_machine.slot_machine_grid[row][col], font=("Helvetica", 24), width=4)
                label.pack(side=tk.LEFT)

    def update_balance_label(self):
        self.balance_label.config(text=f"Balance: ${self.player.total_balance}")

    def play(self):
        if not self.player:
            messagebox.showerror("Error", "You need to start the game first!")
            return

        try:
            ug_row_no = int(self.line_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number between 1 and 6.")
            return

        if ug_row_no not in range(1, 7):
            messagebox.showerror("Error", "Number not in range, please try again.")
            return

        ug_row_no -= 1

        self.slot_machine.spin_slot_machine()
        self.draw_slot_machine()

        first_val = self.slot_machine.slot_machine_grid[ug_row_no][0]
        if all(map(lambda ele: ele == first_val, self.slot_machine.slot_machine_grid[ug_row_no])):
            messagebox.showinfo("Congrats!", "You won! $25 has been deposited to your account.")
            self.player.deposit(25)
        else:
            messagebox.showinfo("Oh No!", "You missed it. $5 has been deducted from your balance.")
            self.player.debit(5)

        self.update_balance_label()

        if not self.player.can_play():
            messagebox.showwarning("Game Over", "You don't have enough balance to continue playing. Ending Game.")
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()