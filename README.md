# python
import random

class NumberGuessingGame:
    def _init_(self, lower=1, upper=100):
        self.lower = lower
        self.upper = upper
        self.number_to_guess = random.randint(self.lower, self.upper)
        self.attempts = 0

    def guess(self, user_guess):
        self.attempts += 1
        if user_guess < self.number_to_guess:
            return "Too low!"
        elif user_guess > self.number_to_guess:
            return "Too high!"
        else:
            return f"Congratulations! You guessed it in {self.attempts} attempts."

    def play(self):
        print(f"Welcome to Number Guessing Game! Guess a number between {self.lower} and {self.upper}.")
        while True:
            try:
                user_input = int(input("Enter your guess: "))
                result = self.guess(user_input)
                print(result)
                if "Congratulations" in result:
                    break
            except ValueError:
                print("Please enter a valid number.")
