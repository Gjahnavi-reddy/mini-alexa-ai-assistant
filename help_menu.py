"""
help_menu.py - Command Guide and Help Menu Module
Nexbridge Technologies - Virtual AI Assistant (Mini Alexa)

Responsibilities:
- Formats and displays the list of all supported commands with concise descriptions (FR-10).
- Guides new users in interacting with the assistant.

AI / Software Engineering Concept:
- Discoverability & Human-Computer Interface: Providing clear affordances so users
  understand the system's operational boundaries and capabilities.
"""


def get_help_text() -> str:
    """
    Constructs a cleanly formatted help string listing all supported commands
    and their corresponding actions.

    Returns:
        str: Formatted help menu.
    """
    help_lines = [
        "Assistant: Here are the commands you can use:",
        "  - time            show current time",
        "  - date            show current date",
        "  - calculate       do a calculation (e.g. 'calculate 12 + 8' or 'calc')",
        "  - joke            tell a programmer or tech joke",
        "  - quote           share an inspirational quote",
        "  - fact            reveal a computer science or AI fact",
        "  - game            play the number guessing game",
        "  - recommend       rule-based activity recommendation (AI concept demo)",
        "  - perceptron      artificial neuron calculation demo (DL concept demo)",
        "  - help            display this command menu",
        "  - exit            quit the assistant (or 'quit', 'bye')",
    ]
    return "\n".join(help_lines)


def print_help() -> None:
    """
    Prints the formatted help menu directly to the console.
    """
    print(get_help_text())
