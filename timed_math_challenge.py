import random
import time

OPERATORS = ["+", "-", "//", "*", "**"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 5

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    expr = str(left) + " " + operator + " " + str(right)
    ans = eval(expr)
    return expr, ans

input("Welcome to timed math challenge! Press enter to start!")
start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, ans = generate_problem()
    while True:
        user_ans = input("Problem # " + str(i+1) + ": " + expr + " = ")
        if user_ans == str(ans):
            print("You got it correct!", expr, "=", ans)
            break

end_time = time.time()
total_time = round(end_time - start_time)
print("Great Job! You finished in", total_time, " seconds!")