import random

def guess_the_number():

    print("Guess the number")
    print("The number is between 1 and 10")

    secret_number = random.randint(1,10)

    attempt = 0

    while True:
        try:
            guess = int(input("Your guess: "))
            if guess < secret_number:
                print("Too low")
                attempt += 1
            elif guess > secret_number:
                print("Too high")
                attempt += 1
            else:
                print("Correct! You guessed the number in", attempt, "turns.")
                break
        except ValueError:
            print("That's not a number")

guess_the_number()
