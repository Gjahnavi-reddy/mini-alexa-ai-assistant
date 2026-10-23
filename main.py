"""
main.py - Virtual AI Assistant (Mini Alexa) Entry Point
Nexbridge Technologies - AI Internship Program (Project 1)

Responsibilities:
- Initialize the assistant session and capture the user's name (FR-01, FR-02).
- Coordinate the primary request-classification-response loop (Sections 15 & 16).
- Route recognized intents to appropriate feature modules (Single Responsibility).
- Fall back gracefully on unrecognized input without crashing (FR-12).
- Provide a clean, polite exit flow (FR-11).

Architecture:
- Flat, procedural console architecture.
- Keyword detection & pattern matching for rule-based intent classification.
"""

import sys
from greetings import (
    build_welcome_banner,
    get_user_name,
    build_greeting,
    build_exit_message,
)
from datetime_utils import get_current_time, get_current_date
from calculator import handle_calculator_command, parse_expression
from content import get_random_quote, get_random_joke, get_random_fact
from game import play_guessing_game
from ai_concepts import recommend_activity, run_perceptron_interactive
from help_menu import print_help


def classify_and_route(user_input: str, user_name: str) -> bool:
    """
    Classifies the user's input text using keyword detection and pattern matching,
    then executes the corresponding feature.

    Intent Classification Strategy:
    - Normalizes input by lowercasing and splitting into tokens/phrases.
    - Matches highest-specificity intents first (Exit, Help, Calculator).
    - Uses token-aware keyword matching for Date, Time, Entertainment, and AI demos.
    - Routes to friendly fallback if no pattern matches.

    Args:
        user_input: Raw string entered by the user.
        user_name: Session-level user name.

    Returns:
        bool: True if the session should continue, False if an exit command was received.
    """
    normalized = user_input.strip().lower()

    if not normalized:
        return True

    words = normalized.split()

    # 1. Exit / Quit commands (FR-11)
    if any(cmd in words for cmd in ("exit", "quit", "bye", "goodbye", "close", "q")):
        print(build_exit_message(user_name))
        return False

    # 2. Help menu (FR-10)
    elif "help" in words or normalized == "?":
        print_help()

    # 3. Calculation command (FR-05)
    # Give priority to math expressions or calc keywords before general time checks
    elif (
        normalized.startswith(("calculate", "calc", "compute", "math"))
        or parse_expression(user_input) is not None
    ):
        result_message = handle_calculator_command(user_input, user_name=user_name)
        print(result_message)

    # 4. Time command (FR-04)
    elif any(w in words for w in ("time", "clock")) or "what time" in normalized:
        print(get_current_time())

    # 5. Date command (FR-03)
    elif any(w in words for w in ("date", "today")) or "day is it" in normalized:
        print(get_current_date())

    # 6. Joke generator (FR-07)
    elif any(w in words for w in ("joke", "jokes", "funny")) or "make me laugh" in normalized:
        print(get_random_joke())

    # 7. Motivational quote (FR-06)
    elif (
        any(w in words for w in ("quote", "quotes", "motivation", "motivate"))
        or "motivat" in normalized
        or "inspire" in normalized
    ):
        print(get_random_quote())

    # 8. Random fact generator (FR-08)
    elif any(w in words for w in ("fact", "facts", "trivia", "knowledge")):
        print(get_random_fact())

    # 9. Number guessing game (FR-09)
    elif any(w in words for w in ("game", "guess", "guessing", "play")):
        play_guessing_game(user_name=user_name)

    # 10. Rule-based recommendation - AI Concept (FR-13)
    elif (
        any(w in words for w in ("recommend", "recommendation", "activity", "routine", "suggest"))
        or "rule" in words
    ):
        print(recommend_activity())

    # 11. Perceptron / Neural Network demo - DL Concept (FR-14)
    elif (
        any(w in words for w in ("perceptron", "neuron", "neural", "dl"))
        or "deep learning" in normalized
    ):
        run_perceptron_interactive(user_name=user_name)

    # 12. Fallback for unrecognized input (FR-12)
    else:
        print(
            f"Assistant: I'm not sure I understood that, {user_name} - "
            f"type 'help' to see what I can do."
        )

    return True


def main() -> None:
    """
    Main program entry point coordinating the session lifecycle.
    """
    # 1. Print Startup Banner
    print(build_welcome_banner())

    # 2. Greet and capture user's name (FR-01, FR-02)
    user_name = get_user_name()

    # 3. Print initial welcome & help hint
    print(build_greeting(user_name))
    print()

    # 4. Main Conversational Loop (HCI input-process-respond cycle)
    while True:
        try:
            raw_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\n" + build_exit_message(user_name))
            break

        # Process input and check if loop should terminate
        keep_running = classify_and_route(raw_input, user_name=user_name)
        print()
        if not keep_running:
            break

    print("===========================================")


if __name__ == "__main__":
    main()
