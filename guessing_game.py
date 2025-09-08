# Start code here
import random
number = random.randint(1, 100)
number_of_guesses = 0
maximum_guesses = 7
while number_of_guesses < maximum_guesses:
    guess = int(input("Guess a number from 1 to 100:"))
    if guess == number:
        print("Correct! You guessed it!")
        print("You guessed in", number_of_guesses, "tries!")
        break
    elif guess > number:
        # The following 3 lines of code were used to stop
        # the hint from being displayed,
        # because the user has already lost the game at 7 guesses
        # and no hints are needed.
        if number_of_guesses == maximum_guesses - 1:
            number_of_guesses = number_of_guesses + 1
            break
        else:
            print("Your guess is higher than the secret number!")
        # The technical bonus question is solved in the following lines,
        # according to your suggested example.
        if number > 50:
            print("Tip: The secret number is between 51 and 100.")
        else:
            print("Tip: The secret number is between 1 and 50.")
    elif guess < number:
        if number_of_guesses == maximum_guesses - 1:
            number_of_guesses = number_of_guesses + 1
            break
        else:
            print("Your guess is lower than the secret number!")
        if number > 50:
            print("Tip: The secret number is between 51 and 100.")
        else:
            print("Tip: The secret number is between 1 and 50.")
    else:
        print("Incorrect! Try again!")
    number_of_guesses = number_of_guesses + 1
# The code below is displayed when the player has lost the game.
# The print was splited in two lines because of the warning from Flake8.
if number_of_guesses == maximum_guesses:
    print("Game over! All", maximum_guesses, "tries were used.")
    print("The secret number was", number, ".")
