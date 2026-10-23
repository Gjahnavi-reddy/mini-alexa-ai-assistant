"""
datetime_utils.py - Date and Time Reporting Utilities
Nexbridge Technologies - Virtual AI Assistant (Mini Alexa)

Responsibilities:
- Retrieve current system date and format as human-readable string (FR-03).
- Retrieve current system time and format as human-readable string (FR-04).

Python Concepts:
- Built-in datetime module: datetime.now(), strftime formatting.
"""

from datetime import datetime


def get_current_time() -> str:
    """
    Fetches the current local system time and formats it into a friendly
    12-hour AM/PM string (e.g., '03:45 PM').

    Returns:
        str: Formatted time string prefixed for the assistant response.
    """
    now = datetime.now()
    formatted_time = now.strftime("%I:%M %p").lstrip("0")
    # In case lstrip removed all zeros (e.g. at 00:xx, though %I is 01-12)
    if not formatted_time.endswith(("AM", "PM")):
        formatted_time = now.strftime("%I:%M %p")
    return f"Assistant: It's currently {formatted_time}."


def get_current_date() -> str:
    """
    Fetches the current local system date and formats it into a full,
    human-readable format (e.g., 'Friday, October 23, 2026').

    Returns:
        str: Formatted date string prefixed for the assistant response.
    """
    now = datetime.now()
    formatted_date = now.strftime("%A, %B %d, %Y")
    return f"Assistant: Today is {formatted_date}."


def get_current_hour() -> int:
    """
    Helper function to get the current hour in 24-hour format (0-23).
    Used by rule-based activity recommendation systems.

    Returns:
        int: Current hour (0 to 23).
    """
    return datetime.now().hour
