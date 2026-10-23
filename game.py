"""
game.py - Number Guessing Game Module
Nexbridge Technologies - Virtual AI Assistant (Mini Alexa)

Responsibilities:
- Implement an interactive number-guessing game with bounded attempts (FR-09).
- Generate a target number using random.randint(1, 20).
- Provide 'higher' / 'lower' feedback hints.
- Handle non-numeric input gracefully without crashing.
- Track remaining attempts and report win/loss outcomes with user personalization.

Algorithmic / Computer Science Concept:
- Binary Search Analogy: Illustrates search spaces and how feedback (higher/lower)
  enables an optimal strategy of halving the remaining hypothesis space.
"""

import random


def play_guessing_game(user_name: str = "Friend", max_attempts: int = 5, lower_bound: int = 1, upper_bound: int = 20) -> None:
    """
    Runs the number guessing game loop.

    Args:
        user_name: Name of the active user for personalized feedback.
        max_attempts: Maximum number of guesses allowed (default: 5).
        lower_bound: Minimum target number (inclusive, default: 1).
        upper_bound: Maximum target number (inclusive, default: 20).
    """
    secret_number = random.randint(lower_bound, upper_bound)
    attempts_used = 0

    print(
        f"Assistant: I'm thinking of a number between {lower_bound} and {upper_bound}. "
        f"You have {max_attempts} tries, {user_name}!"
    )
    print("           (Type 'quit' anytime if you wish to exit the game)\n")

    while attempts_used < max_attempts:
        remaining = max_attempts - attempts_used
        prompt = f"[{user_name}] Guess a number ({remaining} {'try' if remaining == 1 else 'tries'} left): "

        try:
            raw_input = input(prompt).strip()
        except (KeyboardInterrupt, EOFError):
            print("\nAssistant: Game interrupted. Returning to main assistant.")
            return

        # Allow user to gracefully quit the game early
        if raw_input.lower() in ("quit", "exit", "cancel", "q"):
            print(f"Assistant: Game ended early. The secret number was {secret_number}. Thanks for playing, {user_name}!")
            return

        # Input validation for integers
        try:
            guess = int(raw_input)
        except ValueError:
            print("Assistant: Please enter a valid integer! That didn't count as a try.\n")
            continue

        # Range check
        if guess < lower_bound or guess > upper_bound:
            print(f"Assistant: Your guess must be between {lower_bound} and {upper_bound}. Try again!\n")
            continue

        attempts_used += 1

        # Check win condition
        if guess == secret_number:
            print(
                f"\n[WIN] Assistant: Spot on, {user_name}! You guessed the number {secret_number} "
                f"in {attempts_used} {'try' if attempts_used == 1 else 'tries'}! Amazing job!"
            )
            return

        # Give directional feedback
        if attempts_used < max_attempts:
            if guess < secret_number:
                print(f"Assistant: Too low! Try a higher number.")
            else:
                print(f"Assistant: Too high! Try a lower number.")
            print()

    # If all attempts are exhausted
    print(
        f"\nAssistant: Game over! You've used all {max_attempts} tries, {user_name}. "
        f"The secret number was {secret_number}. Better luck next time!"
    )
