#import random libary

import random

# Lists of cars

cars = ["BUGATTI", "LAMBORGHINI", "FERRARI", "PAGANI", "ASTON MARTIN", "MCLAREN", "ROLLS ROYCE", "JAGUAR", "BENTLEY","BMW", "ALFA ROMEO", "MASERATI", "PORSCHE", "AUDI", "RANGE ROVER"]

# selecting a random choice from the cars list

selection = random.choice(cars)

answer = selection

jumble = list(selection)

# jumbler program which scrambles letters

for current_index in range(len(jumble)):
    random_index = random.randrange(0, len(jumble))
    temp = jumble[current_index]
    jumble[current_index] = jumble[random_index]
    jumble[random_index] = temp

for letter in jumble:
    print letter,

# retrieve guess and reply answer
    
guess = 0

while guess != answer:
    guess = raw_input("\nWhat type of car maker is jumbled?\n")
    guess = guess.upper()
    if guess == answer:
        print("It seems you know your cars well.")
    else:
        print("Guess Again...")
