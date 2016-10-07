#import random libary

import random

cars = ["BUGATTI", "LAMBORGHINI", "FERRARI", "PAGANI", "ASTON MARTIN", "MCLAREN", "ROLLS ROYCE", "JAGUAR", "BENTLEY","BMW", "ALFA ROMEO", "MASERATI", "PORSCHE", "AUDI", "RANGE ROVER"]

selection = random.choice(cars)

answer = selection

jumble = list(selection)


for current_index in range(len(jumble)):
    random_index = random.randrange(0, len(jumble))
    temp = jumble[current_index]
    jumble[current_index] = jumble[random_index]
    jumble[random_index] = temp

for letter in jumble:
    print letter,

guess = 0

while guess != answer:
    guess = raw_input("\nWhat type of car maker is jumbled?\n")
    guess = guess.upper()
    if guess == answer:
        print("It seems you know your cars well.")
    else:
        print("Guess Again...")
