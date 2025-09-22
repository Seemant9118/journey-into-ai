# PROJECT 2 – THE PERFECT GUESSING GAME

# How it works

# The class generates a random number (1–100) at the start.

# The user is prompted to guess numbers until they find the correct one.

# After each guess, it gives hints:

# "Lower number please" if the guess is too high.

# "Higher number please" if the guess is too low.

# When guessed correctly, it shows how many attempts were made.

import random

class GuessNumber:
    def __init__(self):
        self.bot_number = random.randint(1, 100)  # computer's number
        self.guess_count = 0                      # track number of guesses

    def check_guess(self, user_number):
        """Check the user's guess against the bot's number."""
        self.guess_count += 1
        if user_number > self.bot_number:
            return "Lower number please"
        elif user_number < self.bot_number:
            return "Higher number please"
        else:
            return f"🎉 Congratulations! You guessed it in {self.guess_count} tries."

# Example usage
if __name__ == "__main__":
    game = GuessNumber()

    while True:
        try:
            user_input = int(input("Enter your guess (1-100): "))
            result = game.check_guess(user_input)
            print(result)
            if "Congratulations" in result:
                break
        except ValueError:
            print("Please enter a valid number between 1 and 100.")
