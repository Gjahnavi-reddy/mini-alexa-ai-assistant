"""
greetings.py - Greeting and User Session Management Module
Nexbridge Technologies - Virtual AI Assistant (Mini Alexa)

Responsibilities:
- Display the application startup banner.
- Capture, sanitize, and store the user's name (FR-01, FR-02).
- Generate personalized greetings, responses, and exit messages.

AI/HCI Concept:
- Human-Computer Interaction (HCI): Establishing a conversational persona and
  maintaining session-level user context/state (simulating memory).
"""


def build_welcome_banner() -> str:
    """
    Returns the formatted ASCII startup banner for Mini Alexa.
    """
    banner = (
        "===========================================\n"
        "        MINI ALEXA - VIRTUAL ASSISTANT     \n"
        "==========================================="
    )
    return banner


def get_user_name() -> str:
    """
    Prompts the user for their name on program startup (FR-01).
    Validates and sanitizes the input, defaulting to 'Friend' if
    the user enters an empty string or whitespace.

    Returns:
        str: Sanitized and title-cased user name.
    """
    prompt = "Assistant: Hi! I'm Mini Alexa. What's your name?\nYou: "
    try:
        raw_name = input(prompt).strip()
    except (KeyboardInterrupt, EOFError):
        raw_name = ""

    # Sanitize and handle empty input gracefully
    if not raw_name:
        sanitized_name = "Friend"
    else:
        # Capitalize appropriately (e.g., 'alex' -> 'Alex')
        sanitized_name = raw_name.title()

    return sanitized_name


def build_greeting(user_name: str) -> str:
    """
    Constructs the initial welcome message after the user's name is captured.

    Args:
        user_name: The remembered name of the user.

    Returns:
        str: Formatted welcome text with guidance.
    """
    return (
        f"Assistant: Nice to meet you, {user_name}! Type 'help'\n"
        f"           to see what I can do."
    )


def build_exit_message(user_name: str) -> str:
    """
    Constructs the personalized farewell message when the session ends (FR-11).

    Args:
        user_name: The remembered name of the user.

    Returns:
        str: Personalized exit greeting.
    """
    return f"Assistant: Goodbye, {user_name}! Have a great day."


def build_personalized_ack(user_name: str, action: str) -> str:
    """
    Utility helper that generates contextual acknowledgments incorporating
    the user's name (FR-02 compliance).

    Args:
        user_name: The user's name.
        action: The task being performed (e.g., 'Here is your quote').

    Returns:
        str: Personalized acknowledgment string.
    """
    return f"Sure thing, {user_name}! {action}"
