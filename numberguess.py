import random

def display_welcome_message():
    print("🎉 Welcome to the Number Guessing Game! 🎉")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is? You have 7 attempts!\n")

def get_user_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100.")
        except ValueError:
            print("That's not a valid number! Please try again.")

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 7
    print("🕵️‍♂️ I have selected a number. Let's see if you can guess it!")

    for attempt in range(1, attempts + 1):
        print(f"\nAttempt {attempt}/{attempts}:")
        guess = get_user_guess()

        if guess < number_to_guess:
            print("📉 Too low! Try again.")
        elif guess > number_to_guess:
            print("📈 Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You've guessed the number {number_to_guess} in {attempt} attempts!")
            break
    else:
        print(f"😞 Sorry, you've used all your attempts. The number was {number_to_guess}.")

def main():
    display_welcome_message()
    while True:
        play_game()
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("👋 Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
