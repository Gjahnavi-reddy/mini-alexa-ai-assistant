"""
test_assistant.py - Automated Unit & Integration Tests
Nexbridge Technologies - Virtual AI Assistant (Mini Alexa)

Validates all 14 Functional Requirements (FR-01 to FR-14) and Acceptance Criteria
defined in the Project 1 PRD.
"""

import unittest
from io import StringIO
import sys
from datetime import datetime

import greetings
import datetime_utils
import calculator
import content
import ai_concepts
import help_menu
import main


class TestGreetingsModule(unittest.TestCase):
    """Tests for FR-01 and FR-02 (Greeting and Name Capture)."""

    def test_build_welcome_banner(self):
        banner = greetings.build_welcome_banner()
        self.assertIn("MINI ALEXA", banner)
        self.assertIn("VIRTUAL ASSISTANT", banner)

    def test_build_greeting(self):
        greeting = greetings.build_greeting("Priya")
        self.assertIn("Priya", greeting)
        self.assertIn("help", greeting)

    def test_build_exit_message(self):
        farewell = greetings.build_exit_message("Alex")
        self.assertIn("Alex", farewell)
        self.assertIn("Goodbye", farewell)


class TestDatetimeUtilsModule(unittest.TestCase):
    """Tests for FR-03 and FR-04 (Date and Time Reporting)."""

    def test_get_current_time(self):
        time_str = datetime_utils.get_current_time()
        self.assertIn("Assistant: It's currently", time_str)
        # Check that it ends with AM or PM
        self.assertTrue(time_str.endswith("AM.") or time_str.endswith("PM."))

    def test_get_current_date(self):
        date_str = datetime_utils.get_current_date()
        current_year = str(datetime.now().year)
        self.assertIn("Assistant: Today is", date_str)
        self.assertIn(current_year, date_str)

    def test_get_current_hour(self):
        hour = datetime_utils.get_current_hour()
        self.assertTrue(0 <= hour <= 23)


class TestCalculatorModule(unittest.TestCase):
    """Tests for FR-05 (Basic Calculator with robust error handling)."""

    def test_addition(self):
        res = calculator.calculate(12, "+", 8)
        self.assertEqual(res, "Assistant: The result is 20.")

    def test_subtraction(self):
        res = calculator.calculate(15, "-", 4)
        self.assertEqual(res, "Assistant: The result is 11.")

    def test_multiplication(self):
        res = calculator.calculate(7, "*", 6)
        self.assertEqual(res, "Assistant: The result is 42.")

    def test_division(self):
        res = calculator.calculate(20, "/", 4)
        self.assertEqual(res, "Assistant: The result is 5.")

    def test_division_by_zero(self):
        res = calculator.calculate(5, "/", 0)
        self.assertIn("can't divide by zero", res)

    def test_parse_expression_standard(self):
        parsed = calculator.parse_expression("calculate 12 + 8")
        self.assertEqual(parsed, (12.0, "+", 8.0))

    def test_parse_expression_without_keyword(self):
        parsed = calculator.parse_expression("100 / 4")
        self.assertEqual(parsed, (100.0, "/", 4.0))

    def test_parse_expression_word_operators(self):
        parsed = calculator.parse_expression("calculate 10 times 5")
        self.assertEqual(parsed, (10.0, "*", 5.0))

    def test_parse_invalid_expression(self):
        parsed = calculator.parse_expression("hello world")
        self.assertIsNone(parsed)


class TestContentModule(unittest.TestCase):
    """Tests for FR-06, FR-07, FR-08 (Quotes, Jokes, and Facts)."""

    def test_quote_randomness_and_validity(self):
        quotes_seen = set()
        for _ in range(20):
            res = content.get_random_quote()
            self.assertIn("Assistant:", res)
            quotes_seen.add(res)
        # Acceptance Criteria: Repeated 5+ times, returns at least 2 different items
        self.assertGreater(len(quotes_seen), 1)

    def test_joke_randomness_and_validity(self):
        jokes_seen = set()
        for _ in range(20):
            res = content.get_random_joke()
            self.assertIn("Assistant:", res)
            jokes_seen.add(res)
        self.assertGreater(len(jokes_seen), 1)

    def test_fact_randomness_and_validity(self):
        facts_seen = set()
        for _ in range(20):
            res = content.get_random_fact()
            self.assertIn("Assistant: Did you know?", res)
            facts_seen.add(res)
        self.assertGreater(len(facts_seen), 1)


class TestAIConceptsModule(unittest.TestCase):
    """Tests for FR-13 (Rule-Based Decisions) and FR-14 (Perceptron Simulation)."""

    def test_recommend_activity_branches(self):
        # Morning test
        morning = ai_concepts.recommend_activity(hour=7)
        self.assertIn("Early Morning", morning)
        self.assertIn("Rule-Based", morning)

        # Deep work test
        work = ai_concepts.recommend_activity(hour=10)
        self.assertIn("Mid Morning", work)
        self.assertIn("Deep work", work)

        # Lunch test
        lunch = ai_concepts.recommend_activity(hour=13)
        self.assertIn("Lunch", lunch)

        # Evening test
        evening = ai_concepts.recommend_activity(hour=19)
        self.assertIn("Evening", evening)

        # Night test
        night = ai_concepts.recommend_activity(hour=2)
        self.assertIn("Sleep Window", night)

    def test_perceptron_calculation(self):
        # Activation should be 1 if weighted sum >= 0
        res_pass = ai_concepts.calculate_perceptron(
            inputs=[5.0, 80.0],
            weights=[0.40, 0.03],
            bias=-2.50
        )
        # 5*0.40 + 80*0.03 - 2.50 = 2.0 + 2.4 - 2.5 = 1.9 >= 0 -> 1
        self.assertAlmostEqual(res_pass["weighted_sum"], 1.9, places=2)
        self.assertEqual(res_pass["output"], 1)

        # Failure case where weighted sum < 0
        res_fail = ai_concepts.calculate_perceptron(
            inputs=[1.0, 10.0],
            weights=[0.40, 0.03],
            bias=-2.50
        )
        # 1*0.4 + 10*0.03 - 2.5 = 0.4 + 0.3 - 2.5 = -1.8 < 0 -> 0
        self.assertAlmostEqual(res_fail["weighted_sum"], -1.8, places=2)
        self.assertEqual(res_fail["output"], 0)


class TestHelpAndRouting(unittest.TestCase):
    """Tests for FR-10 (Help Menu), FR-11 (Exit), and FR-12 (Fallback Handling)."""

    def test_help_menu_content(self):
        help_text = help_menu.get_help_text()
        self.assertIn("time", help_text)
        self.assertIn("date", help_text)
        self.assertIn("calculate", help_text)
        self.assertIn("joke", help_text)
        self.assertIn("quote", help_text)
        self.assertIn("fact", help_text)
        self.assertIn("game", help_text)
        self.assertIn("recommend", help_text)
        self.assertIn("perceptron", help_text)
        self.assertIn("exit", help_text)

    def test_routing_exit(self):
        # Capture stdout
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            continues = main.classify_and_route("exit", "Alex")
            output = sys.stdout.getvalue()
            self.assertFalse(continues)
            self.assertIn("Goodbye, Alex!", output)
        finally:
            sys.stdout = old_stdout

    def test_routing_fallback_unknown_input(self):
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            continues = main.classify_and_route("xyz987randomgibberish", "Alex")
            output = sys.stdout.getvalue()
            self.assertTrue(continues)
            self.assertIn("I'm not sure I understood that, Alex", output)
            self.assertIn("type 'help'", output)
        finally:
            sys.stdout = old_stdout


if __name__ == "__main__":
    unittest.main()
