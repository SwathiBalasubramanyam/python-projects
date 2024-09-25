import random
import string

def generate_password(min_len, numbers=True, special_chars=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    chars = letters
    if numbers:
        chars += digits

    if special_chars:
        chars += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_len:
        rand_char = random.choice(chars)

        pwd += rand_char
        if rand_char in digits:
            has_number = True
        elif rand_char in special:
            has_special = True


        meets_criteria = True
        if numbers:
            meets_criteria = has_number

        if special_chars:
            meets_criteria = meets_criteria and has_special

    return pwd

min_len = int(input("Please enter min len for pwd"))
allow_nums = input("do you want to have numbers in your pwd? y/n ").lower() == "y"
allow_special = input("do you want to have special chars? (y/n)").lower() == "y"

print(generate_password(10, allow_nums, allow_special))