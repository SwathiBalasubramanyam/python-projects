import turtle
import time
import random

class RacerObject:

    def __init__(self, color, x_cord, y_cord):
        self.racer = turtle.Turtle()
        self.racer.color(color)
        self.racer.shape("turtle")
        self.racer.left(90)
        self.racer.penup()
        self.racer.setpos(x_cord, y_cord)
        self.racer.pendown()

class TurtleRace:
    WIDTH = 500
    HEIGHT = 500
    OFFSET = 10
    COLORS = ['red', 'blue', 'green', 'yellow', 'purple', 'pink', 'orange', 'black', 'brown', 'cyan']
    SPEED = [0,10,6,3,1]

    def __init__(self):
        self.num_racers = int(input("enter the number of racers (2-10): "))
        self.setup_canvas_screen()
        self.colors = self.COLORS.copy()
        random.shuffle(self.colors)
        self.start_y = ((self.HEIGHT//2) * -1) + self.OFFSET
        self.x_space = self.WIDTH//(self.num_racers+1)
        self.start_x = (self.WIDTH//2) * -1
        self.racers = []
        self.setup_racers()
        self.race_over = False
        self.race()

    def setup_canvas_screen(self):
        self.canvas_screen = turtle.Screen()
        self.canvas_screen.setup(self.WIDTH, self.HEIGHT)
        self.canvas_screen.title('Turtle Racing!')

    def setup_racers(self):
        for idx in range(self.num_racers):
            self.start_x += self.x_space
            self.racers.append(RacerObject(self.colors[idx], self.start_x, self.start_y))

    def race(self):
        while not self.race_over:
            for idx, racer in enumerate(self.racers):
                racer.racer.forward(random.randrange(1, 20))
                if racer.racer.pos()[1] >= self.HEIGHT//2-self.OFFSET:
                    self.race_over = self.colors[idx]
                    self.display_race_over_message()
                    break

    def display_race_over_message(self):
        if not self.race_over:
            return
        
        self.canvas_screen.reset()
        message = turtle.Turtle()
        message.penup()
        message.write(f"Turtle with color {self.race_over} won the race!", align="center", font=("Arial", 20, "normal"))
        time.sleep(1)
            
game = TurtleRace()
