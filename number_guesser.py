import random

top_of_range = input("Type a number:\n")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0.")
        quit()
else:
    print("Please enter a valid number.")
    quit()

random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses +=1
    user_guess = input("Try to guess the number.\n")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please enter a valid number.")
        continue

    if user_guess == random_number:
        print("You guessed correctly!")
        print("You got it right after", guesses, "guesses")
        break
    elif user_guess > random_number:
        print("Your guess is to high")
    else:
        print("Your guess is to low")
