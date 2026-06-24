import random

def get_user_guess():
    """Prompt the user for a guess and validate the input."""
    while True:
        try:
            guess = int(input("Enter your guess (1-100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("⚠️  Please enter a number between 1 and 100.")
        except ValueError:
            print("⚠️  Invalid input! Please enter a whole number.")


def play_game():
    """Main game logic for the Number Guessing Game."""
    MAX_ATTEMPTS = 7

    print("=" * 45)
    print("   🎯 Welcome to the Number Guessing Game!")
    print("=" * 45)
    print(f"I've picked a secret number between 1 and 100.")
    print(f"You have {MAX_ATTEMPTS} attempts to guess it. Good luck!\n")

    secret_number = random.randint(1, 100)
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        remaining = MAX_ATTEMPTS - attempts
        print(f"Attempts remaining: {remaining}")

        guess = get_user_guess()
        attempts += 1

        if guess == secret_number:
            print(f"\n🎉 Congratulations! You guessed it in {attempts} attempt(s)!")
            print(f"The secret number was: {secret_number}")
            break
        elif guess < secret_number:
            print("📉 Too low! Try a higher number.\n")
        else:
            print("📈 Too high! Try a lower number.\n")

    else:
        print(f"\n😢 Game Over! You've used all {MAX_ATTEMPTS} attempts.")
        print(f"The secret number was: {secret_number}")


def main():
    while True:
        play_game()
        print("\nWould you like to play again?")
        choice = input("Enter 'yes' to play again or anything else to quit: ").strip().lower()
        if choice != 'yes':
            print("\nThanks for playing! Goodbye! 👋")
            break
        print()


if __name__ == "__main__":
    main()
