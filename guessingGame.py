import random

print("Guessing the number!")

number = random.randint(1,9)
chances = 0

print("Try to guess a number between 1 and 9!")
print("You will ony get 5 chances")

while chances < 5:
    guess = int(input("Type your guess: "))

    if guess == number:
        print("Bravo, you guessed the right number!!")
        chances=5

    elif guess > number:
        print("Oh! Your guess was too high.")
    else:
        print("Oh! Your guess was too low.")

    chances= chances + 1

if chances > 5:
    print("Thank you for playing the game")
    print("The number was: ", number)
