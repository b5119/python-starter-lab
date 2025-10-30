"""
Number Guessing Game
A simple game where the computer picks a random number and you guess it.
Uses while loops for game logic.
"""
import random

def play_game():
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    print("🎮 Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100.")
    print(f"You have {max_attempts} attempts.\n")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1
            
            if guess < number:
                print("📈 Too low! Try again.\n")
            elif guess > number:
                print("📉 Too high! Try again.\n")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                return True
                
        except ValueError:
            print("❌ Please enter a valid number.\n")
            attempts -= 1
    
    print(f"😢 Game Over! The number was {number}")
    return False

def main():
    play_again = True
    
    while play_again:
        play_game()
        response = input("\nWould you like to play again? (yes/no): ").lower()
        play_again = response in ['yes', 'y']
    
    print("Thanks for playing! 👋")

if __name__ == "__main__":
    main()