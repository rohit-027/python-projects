import random

number = random.randint(1, 10)
your_chance = 5

while(your_chance > 0):
    your_guess = int(input("Guess the number between 1 and 10: "))
    if(number == your_guess):
        print("You Won!")
        break

    else:
        print(f"That was wrong. You have {your_chance - 1} chance left to guess the correct number: ")

    your_chance -= 1

    if(your_guess != number):
        print("You Loose!!" )