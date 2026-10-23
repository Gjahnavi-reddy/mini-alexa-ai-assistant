"""
test_interactive_features.py - Automated Testing for Interactive Sub-modes
Nexbridge Technologies - Virtual AI Assistant (Mini Alexa)

Validates interactive components:
- game.py: play_guessing_game() with simulated inputs (invalid input, too high/low hints, win/quit)
- ai_concepts.py: run_perceptron_interactive() modes (student predictor, custom, 2-layer network)
- calculator.py: interactive step-by-step calculator prompts
"""

import unittest
from unittest.mock import patch
from io import StringIO

import game
import ai_concepts
import calculator


class TestInteractiveFeatures(unittest.TestCase):
    """Test interactive sub-loops using mock inputs."""

    @patch("builtins.input", side_effect=["invalid_text", "99", "quit"])
    def test_game_invalid_and_quit(self, mock_input):
        old_stdout = StringIO()
        with patch("sys.stdout", old_stdout):
            game.play_guessing_game(user_name="Alex", max_attempts=5)
        output = old_stdout.getvalue()
        self.assertIn("valid integer", output)
        self.assertIn("between 1 and 20", output)
        self.assertIn("Game ended early", output)

    @patch("builtins.input", side_effect=["10"])
    @patch("random.randint", return_value=10)
    def test_game_immediate_win(self, mock_rand, mock_input):
        old_stdout = StringIO()
        with patch("sys.stdout", old_stdout):
            game.play_guessing_game(user_name="Priya", max_attempts=5)
        output = old_stdout.getvalue()
        self.assertIn("[WIN]", output)
        self.assertIn("Spot on, Priya!", output)

    @patch("builtins.input", side_effect=["1", "5", "80"])
    def test_perceptron_student_predictor(self, mock_input):
        old_stdout = StringIO()
        with patch("sys.stdout", old_stdout):
            ai_concepts.run_perceptron_interactive(user_name="Alex")
        output = old_stdout.getvalue()
        self.assertIn("Student Exam Predictor", output)
        self.assertIn("Forward Propagation Steps", output)
        self.assertIn("[PASS]", output)

    @patch("builtins.input", side_effect=["2", "2.0", "0.5", "1.0", "-0.2", "-0.5"])
    def test_perceptron_custom_calculation(self, mock_input):
        old_stdout = StringIO()
        with patch("sys.stdout", old_stdout):
            ai_concepts.run_perceptron_interactive(user_name="Alex")
        output = old_stdout.getvalue()
        self.assertIn("Custom Perceptron Experiment", output)
        self.assertIn("Weighted Sum (z):", output)

    @patch("builtins.input", side_effect=["3", "1.0", "0.5"])
    def test_perceptron_hidden_layer_demo(self, mock_input):
        old_stdout = StringIO()
        with patch("sys.stdout", old_stdout):
            ai_concepts.run_perceptron_interactive(user_name="Alex")
        output = old_stdout.getvalue()
        self.assertIn("Hidden Layer & Multi-Neuron Network Demo", output)
        self.assertIn("Forward Propagation Walkthrough", output)

    @patch("builtins.input", side_effect=["12 + 8"])
    def test_calculator_interactive_expression(self, mock_input):
        old_stdout = StringIO()
        with patch("sys.stdout", old_stdout):
            res = calculator.handle_calculator_command("calculate", user_name="Alex")
        self.assertEqual(res, "Assistant: The result is 20.")

    @patch("builtins.input", side_effect=["bad_expr", "15", "*", "4"])
    def test_calculator_interactive_step_by_step(self, mock_input):
        old_stdout = StringIO()
        with patch("sys.stdout", old_stdout):
            res = calculator.handle_calculator_command("calc", user_name="Alex")
        self.assertEqual(res, "Assistant: The result is 60.")


if __name__ == "__main__":
    unittest.main()
