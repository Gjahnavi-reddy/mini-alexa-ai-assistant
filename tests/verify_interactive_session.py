"""
verify_interactive_session.py - Simulated End-to-End Session Test
Nexbridge Technologies - Virtual AI Assistant (Mini Alexa)

Simulates 20+ user interactions through main.py to verify reliability,
graceful handling of invalid inputs, and compliance with PRD Acceptance Criteria.
"""

import subprocess
import sys


def run_simulated_session():
    # Sequence of inputs to feed to the assistant via stdin
    test_inputs = [
        "Priya",                      # FR-01: Name capture
        "help",                       # FR-10: Help menu
        "time",                       # FR-04: Current time
        "date",                       # FR-03: Current date
        "calculate 12 + 8",           # FR-05: Addition
        "calculate 50 / 5",           # FR-05: Division
        "calculate 5 / 0",            # FR-05: Division by zero handling
        "calculate 10 times 4",       # FR-05: Word operator multiplication
        "100 - 35",                   # FR-05: Direct arithmetic expression
        "joke",                       # FR-07: Joke
        "quote",                      # FR-06: Motivational quote
        "fact",                       # FR-08: Fact
        "recommend",                  # FR-13: Rule-based recommendation
        "asdkfj",                     # FR-12: Unrecognized input fallback
        "!!!???",                     # FR-12: Punctuation fallback
        "what is the time please",    # Intent keyword matching ('time')
        "tell me a funny joke",       # Intent keyword matching ('joke')
        "can you inspire me",         # Intent keyword matching ('inspire')
        "exit"                        # FR-11: Clean exit
    ]

    input_payload = "\n".join(test_inputs) + "\n"

    process = subprocess.Popen(
        [sys.executable, "main.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace"
    )

    stdout, stderr = process.communicate(input=input_payload)

    print("==================================================")
    print("        END-TO-END SIMULATED SESSION OUTPUT       ")
    print("==================================================")
    print(stdout)

    if stderr:
        print("STDERR OUTPUT (Errors encountered):")
        print(stderr)

    # Check key requirements in the session output
    assertions = [
        ("Banner displayed", "MINI ALEXA - VIRTUAL ASSISTANT" in stdout),
        ("User name used in greeting", "Nice to meet you, Priya!" in stdout),
        ("Help menu displayed", "Here are the commands you can use" in stdout),
        ("Time displayed", "It's currently" in stdout),
        ("Date displayed", "Today is" in stdout),
        ("Calculation 12+8=20", "The result is 20" in stdout),
        ("Calculation 50/5=10", "The result is 10" in stdout),
        ("Division by zero friendly error", "I can't divide by zero" in stdout),
        ("Word operator 10*4=40", "The result is 40" in stdout),
        ("Direct math 100-35=65", "The result is 65" in stdout),
        ("Rule-based recommendation", "Rule-Based AI Recommendation" in stdout),
        ("Fallback handling for unknown input", "I'm not sure I understood that, Priya" in stdout),
        ("Graceful exit message with user name", "Goodbye, Priya! Have a great day." in stdout),
    ]

    print("\n================ VERIFICATION CHECKS ================")
    all_passed = True
    for name, passed in assertions:
        status = "PASSED" if passed else "FAILED"
        print(f"[{status}] {name}")
        if not passed:
            all_passed = False

    print("=====================================================")
    if all_passed:
        print("ALL 13 VERIFICATION CRITERIA PASSED WITHOUT ERRORS!")
    else:
        print("SOME VERIFICATION CRITERIA FAILED.")

    return all_passed


if __name__ == "__main__":
    success = run_simulated_session()
    if not success:
        sys.exit(1)
