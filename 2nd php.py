import random

def guess_the_number():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Welcome to the Guess the Number Game!")
    print("I have selected a number between 1 and 100.")
    
    while not guessed:
        # Ask the user for their guess
        user_guess = input("Please enter your guess: ")
        
        # Validate the input
        if not user_guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        user_guess = int(user_guess)
        attempts += 1
        
        # Check if the guess is correct
        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed = True
            print(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")

# Run the game
guess_the_number()
