# name = "Alice"
# age = 25
# is_student = True

import random

def guessing_game():
    number = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    while True:
        guess = input("Make a guess: ")
        
        # Check if input is a number
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)
        attempts += 1
        
        if guess < number:
            print("Too low. Try again!")
        elif guess > number:
            print("Too high. Try again!")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            break

if __name__ == "__main__":
    guessing_game()
