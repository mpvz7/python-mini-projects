import random

def guessing_game():
    print("Welcome to the Number Guessing Game!")

    number = random.randint(1, 100)
    print("\nI'm thinking of a number between 1 and 100. Can you guess it?")

    attempts = 0
    
    while True:
        
        guess = input("\nEnter your guess (or 'q' to quit): ")
        
        if guess == 'q':
            print(f"\nThe number was {number}.")
            break
        
        try:
            attempts += 1
            guess = int(guess)
            
            if guess < number:
                print("Too low.")
            elif guess > number:
                print("Too high.")
            else:
                print(f"\nCongratulations! You guessed the number in {attempts} attempts.")
                break
            
        except ValueError:
            print("Please enter a valid number or 'q' to quit.")

if __name__ == "__main__":
    guessing_game()