"""
calculator.py - Arithmetic Parsing and Calculation Module
Nexbridge Technologies - Virtual AI Assistant (Mini Alexa)

Responsibilities:
- Parse arithmetic expressions containing two operands and an operator (FR-05).
- Perform basic operations: Addition (+), Subtraction (-), Multiplication (*), Division (/).
- Handle division by zero and invalid inputs gracefully without crashing (Reliability).

Python Concepts:
- String manipulation (split, strip, replace).
- Exception handling: try/except blocks (ValueError, ZeroDivisionError).
- Clean mathematical formatting.
"""

from typing import Optional, Tuple


def calculate(num1: float, operator: str, num2: float) -> str:
    """
    Performs arithmetic calculation given two numbers and an operator.

    Args:
        num1: First numeric operand.
        operator: String representing the operator (+, -, *, /).
        num2: Second numeric operand.

    Returns:
        str: Assistant response message with result or error description.
    """
    try:
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator in ("*", "x", "X"):
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                return "Assistant: I can't divide by zero - try a different number."
            result = num1 / num2
        else:
            return f"Assistant: Unsupported operator '{operator}'. Please use +, -, *, or /."

        # Format integer results neatly (e.g., 20 instead of 20.0)
        if isinstance(result, float) and result.is_integer():
            formatted_result: str | int = int(result)
        else:
            formatted_result = round(result, 4)

        return f"Assistant: The result is {formatted_result}."

    except ZeroDivisionError:
        return "Assistant: I can't divide by zero - try a different number."
    except Exception as err:
        return f"Assistant: Calculation error: {err}"


def parse_expression(text: str) -> Optional[Tuple[float, str, float]]:
    """
    Parses a string containing an arithmetic expression.
    Supports formats like:
      - '12 + 8'
      - 'calculate 12 + 8'
      - '5.5 * 2'
      - '10 / 2'
      - '15 - 4'
      - 'calculate 10 plus 5'

    Args:
        text: Input string from user.

    Returns:
        Tuple of (num1, operator, num2) if successfully parsed, None otherwise.
    """
    # Remove leading command keywords
    cleaned = text.strip()
    for prefix in ["calculate", "calc", "compute"]:
        if cleaned.lower().startswith(prefix):
            cleaned = cleaned[len(prefix):].strip()
            break

    # Normalize word-based operators
    replacements = {
        " plus ": " + ",
        " add ": " + ",
        " minus ": " - ",
        " subtract ": " - ",
        " times ": " * ",
        " multiplied by ": " * ",
        " divide by ": " / ",
        " divided by ": " / ",
        " over ": " / ",
    }
    lowered = " " + cleaned.lower() + " "
    for word, sym in replacements.items():
        if word in lowered:
            lowered = lowered.replace(word, sym)
            cleaned = lowered.strip()
            break

    # Look for standard operators: +, -, *, /
    operators = ["+", "-", "*", "/", "x", "X"]
    found_op = None
    op_index = -1

    # Check for spaced operators first (e.g., '12 + 8' or '-5 + 3')
    for op in [" + ", " - ", " * ", " / ", " x ", " X "]:
        if op in cleaned:
            parts = cleaned.split(op, 1)
            try:
                n1 = float(parts[0].strip())
                n2 = float(parts[1].strip())
                return n1, op.strip(), n2
            except ValueError:
                pass

    # If no spaced operator matched, scan character by character
    # Skipping the first char in case it's a negative sign (e.g. -5 + 2)
    for i in range(1, len(cleaned)):
        char = cleaned[i]
        if char in operators:
            found_op = char
            op_index = i
            break

    if found_op is not None and op_index > 0:
        part1 = cleaned[:op_index].strip()
        part2 = cleaned[op_index + 1:].strip()
        try:
            n1 = float(part1)
            n2 = float(part2)
            return n1, found_op, n2
        except ValueError:
            return None

    return None


def handle_calculator_command(user_input: str, user_name: str = "Friend") -> str:
    """
    Main entry point for handling calculator requests.
    Supports both direct inline expressions ('calculate 12 + 8') and
    interactive step-by-step prompts if only 'calculate' was entered.

    Args:
        user_input: The raw command string.
        user_name: User's name for personalization.

    Returns:
        str: Assistant's response string.
    """
    # Try parsing inline expression first
    parsed = parse_expression(user_input)
    if parsed is not None:
        num1, op, num2 = parsed
        return calculate(num1, op, num2)

    # If user just typed 'calculate' or 'calc' without an expression,
    # prompt interactively with full exception handling
    print(f"Assistant: Sure, {user_name}! Let's do some math.")
    try:
        expr_prompt = input("Enter an expression (e.g., 12 + 8): ").strip()
        parsed_interactive = parse_expression(expr_prompt)
        if parsed_interactive is not None:
            n1, op, n2 = parsed_interactive
            return calculate(n1, op, n2)

        # Fallback to step-by-step input if inline parse fails
        print("Assistant: Could not parse expression directly. Let's do it step-by-step:")
        raw_n1 = input("  Enter first number: ").strip()
        n1 = float(raw_n1)

        op = input("  Enter operator (+, -, *, /): ").strip()
        if op not in ("+", "-", "*", "/", "x", "X"):
            return f"Assistant: Invalid operator '{op}'. Supported operators are +, -, *, /."

        raw_n2 = input("  Enter second number: ").strip()
        n2 = float(raw_n2)

        return calculate(n1, op, n2)

    except ValueError:
        return "Assistant: Invalid number entered. Please enter numeric values only."
    except (KeyboardInterrupt, EOFError):
        return "Assistant: Calculation cancelled."
