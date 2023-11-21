import random


def is_numeric(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


# Generate a random correct guess between 1 and 20
correct_guess = random.randint(1, 20)

while True:
    # Ask the user to guess the number
    user_guess = input("Guess the number between 1 and 20: ")

    # Check if the input is a valid number
    if not is_numeric(user_guess):
        print("Invalid input. Please enter a valid number.")
        continue  # Go back to the start of the loop

    # Convert the user's guess to an integer
    user_guess = int(user_guess)

    # Check if the user's guess is correct
    if user_guess == correct_guess:
        print("Congratulations! You guessed the correct number.")
        break  # Exit the loop because the guess is correct
    else:
        print("Sorry, that's not the right number. Try again.")
