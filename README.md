# Mini Alexa - Virtual AI Assistant 🤖

Hey there! Welcome to **Mini Alexa**, a lightweight, terminal-based virtual assistant built in pure Python.

This project was built for **Project 1 of the Nexbridge Technologies AI Internship Program**. The goal was to build a clean, reliable, and modular command-line assistant from scratch without using any third-party packages, APIs, or heavy ML libraries. Everything runs 100% offline using just Python's built-in standard library!

---

## 💡 What Can Mini Alexa Do?

Even though it runs entirely in the terminal, Mini Alexa comes packed with handy utilities, fun easter eggs, and interactive AI demos:

- 👤 **Personalized Greetings**: Remembers your name throughout the session and addresses you naturally.
- 🕒 **Time & Date**: Checks your system clock and calendar with friendly formatting.
- 🧮 **Built-in Calculator**: Handles inline math (like `calculate 12 + 8` or `100 - 35`), word-based operators (like `10 times 4`), and prompts you step-by-step if you just type `calc`. It won't crash if you divide by zero or enter bad input!
- 🎲 **Number Guessing Game**: An interactive mini-game where the assistant picks a secret number between 1 and 20. You get 5 attempts with helpful "too high" or "too low" hints.
- 😄 **Jokes, Quotes & Tech Facts**: Randomly pulls from a curated collection of programming jokes, inspirational quotes from tech pioneers, and computing trivia.
- 🌳 **Rule-Based Decision Demo (AI)**: Recommends what you should be doing based on the time of day, illustrating how early rule-based expert systems and decision trees work.
- 🧠 **Perceptron Simulation (Deep Learning)**: Demonstrates the exact math behind an artificial neuron (inputs, weights, bias, and step activation) with an exam pass predictor and a custom experimenter.
- 🛡️ **Crash-Proof Design**: Handles unexpected input, typos, and `Ctrl+C` gracefully without throwing messy tracebacks.

---

## 🚀 Quick Start

No virtual environments, no `pip install`, and no API keys required!

### Requirements
- **Python 3.8+** (tested on Python 3.12)

### Running the Assistant
Open your terminal inside the project folder and run:

```bash
python main.py
```

That's it! Mini Alexa will greet you, ask for your name, and you can start typing commands.

---

## 💬 Commands You Can Try

Here are some example inputs to try once the assistant is running:

| Command | What it does | Examples to try |
|---|---|---|
| `help` | Shows the list of available commands | `help` or `?` |
| `time` | Tells you the current time | `time`, `what time is it?` |
| `date` | Gives today's full date | `date`, `what's the date today?` |
| `calculate` | Solves math problems | `calculate 12 + 8`, `50 / 5`, `10 times 4`, `calc` |
| `joke` | Tells a programmer joke | `joke`, `tell me a joke`, `funny` |
| `quote` | Shares an inspiring quote | `quote`, `inspire me` |
| `fact` | Drops a cool tech/AI trivia fact | `fact`, `tell me a fact` |
| `game` | Starts the 1–20 number guessing game | `game`, `play`, `guess` |
| `recommend`| Recommends an activity based on the hour | `recommend`, `activity`, `routine` |
| `perceptron`| Launches the artificial neuron simulator | `perceptron`, `neuron`, `dl` |
| `exit` | Says goodbye and ends the session | `exit`, `quit`, `bye`, `goodbye` |

---

## 🛠️ How It Works (Project Architecture)

I broke the code down into 8 focused modules so every file has one clear job:

```
c:/Virtual AI Assitant/
├── main.py                     # The brain - runs the main loop and routes user input
├── greetings.py                # Handles startup banners, name capture, and friendly goodbyes
├── datetime_utils.py           # Clean date and time reporting using Python's datetime module
├── calculator.py               # Math logic, expression parsing, and divide-by-zero protection
├── content.py                  # Curated lists of quotes, jokes, and facts with random selection
├── game.py                     # Number guessing game loop with attempts tracking and hints
├── ai_concepts.py              # Rule-based decision tree and Perceptron math simulations
├── help_menu.py                # Command menu formatting and user guidance
├── test_assistant.py           # 23 automated unit and integration tests
├── test_interactive_features.py# 7 mock-input tests for interactive games and sub-prompts
├── verify_interactive_session.py# End-to-end multi-turn session verification script
└── README.md                   # You are here!
```

### The Request-Response Cycle

On every turn, the assistant follows a simple, clean workflow:

1. **Read & Clean Input**: Takes what you typed, strips extra spaces, and converts it to lowercase.
2. **Intent Matching**: Checks for keywords or math patterns to figure out what you want to do.
3. **Execute Feature**: Calls the appropriate module function.
4. **Respond & Loop**: Prints the result with your name included where appropriate, then waits for your next command. If you type an exit word (`quit`, `exit`, `bye`), it breaks the loop and closes cleanly.

---

## 🧠 Connecting the Code to AI Concepts

One of the coolest parts of this project was connecting basic Python concepts to real AI fundamentals:

### 1. Rule-Based Systems & Decision Trees (`ai_concepts.py`)
Before deep learning took over, AI was primarily "rule-based" — experts wrote explicit if-then rules to guide computer decisions.
- In `recommend_activity()`, the assistant checks `hour` against a chain of `if-elif-else` branches (Morning, Deep Work, Lunch, Collaboration, Evening, Sleep).
- This directly mirrors how a **Decision Tree** classifier splits on numeric features to assign an input to an outcome category.

### 2. Intent Recognition & Keyword Spotting (`main.py`)
Real conversational agents like Siri or Alexa need to turn raw text into a specific "intent" (e.g., asking for the weather, setting a timer).
- In `main.py`, the `classify_and_route()` function acts as an intent classifier. It cleans the text and prioritizes high-confidence patterns (like math operators and explicit command words) before checking general phrases.
- It also has a reliable fallback (`FR-12`) so typing gibberish gives a polite hint instead of crashing the program.

### 3. The Artificial Neuron (Perceptron) (`ai_concepts.py`)
A Perceptron is the simplest form of a neural network, first invented by Frank Rosenblatt back in 1958.
Rather than using a black-box framework like PyTorch, I implemented the forward pass directly with plain Python arithmetic:

```
Inputs (x)          Weights (w)
[ Study Hours ] ----( w1 = +0.40 )----\
                                       +---> [ Weighted Sum: (w*x) + b ] ---> [ Step Function (>=0) ] ---> Output (1=Pass, 0=Fail)
[ Attendance% ] ----( w2 = +0.03 )----/
[ Bias (b) ]   ----(   b = -2.50 )---/
```

- **Inputs ($x$):** The features we observe (e.g., study hours, attendance).
- **Weights ($w$):** How important each feature is to the final decision.
- **Bias ($b$):** The baseline threshold that the weighted inputs must overcome.
- **Weighted Sum ($z$):** Multiply each input by its weight, sum them all up, and add the bias.
- **Step Activation:** If $z \ge 0$, the neuron fires (`1`). If $z < 0$, it stays inactive (`0`).

When you run `perceptron`, you can test an interactive student pass predictor, enter your own custom weights/bias, or view a 2-layer forward propagation walkthrough!

---

## 🧪 Testing & Verification

Reliability is a big priority for this project. Invalid inputs (like dividing by zero, passing letters into the guessing game, or typing strange punctuation) should never crash the app.

I wrote comprehensive automated tests using Python's built-in `unittest` module:

### Run all 30 automated tests:
```bash
python -m unittest discover
```
*(All 30 tests run in less than 0.01 seconds and test every feature from FR-01 through FR-14).*

### Run the end-to-end conversation simulation:
```bash
python verify_interactive_session.py
```
*(This script spins up a real session, feeds 20+ different user turns through stdin, and asserts that every single response is correct).*

---

## 📝 Sample Terminal Session

Here is what an actual conversation looks like in action:

```text
===========================================
        MINI ALEXA - VIRTUAL ASSISTANT     
===========================================
Assistant: Hi! I'm Mini Alexa. What's your name?
You: Priya
Assistant: Nice to meet you, Priya! Type 'help'
           to see what I can do.

You: time
Assistant: It's currently 1:29 PM.

You: date
Assistant: Today is Friday, October 23, 2026.

You: calculate 12 + 8
Assistant: The result is 20.

You: calculate 5 / 0
Assistant: I can't divide by zero - try a different number.

You: joke
Assistant: Why did the neural network cross the road? To optimize its loss function on the other side.

You: recommend
Assistant: [Rule-Based AI Recommendation]
  * Current Time Reference: 13:00 (Afternoon Lunch)
  * Recommended Activity: Lunch break, hydration, and stepping away from screens.
  * Cognitive Focus: Recharge your mental energy.

  [AI Concept Note]: This feature simulates a Rule-Based Expert System.
  It maps input feature 'hour=13' to an output class using an explicit
  deterministic decision tree with if-elif conditions.

You: exit
Assistant: Goodbye, Priya! Have a great day.
===========================================
```

---

## 🎓 Key Takeaways

Building this first project helped solidify several important software engineering and AI practices:
1. **Structuring a multi-file Python project**: Keeping concerns separated makes debugging and testing ten times easier.
2. **Defensive programming**: Always expecting users to enter invalid data (strings instead of ints, dividing by zero, hitting Ctrl+C) and handling those gracefully.
3. **Demystifying AI/DL concepts**: Realizing that neural networks and decision trees aren't magic — at their foundation, they start with clean math, conditional logic, and iterative processing.

*Thanks for checking out the project! Feel free to explore the code in each module.*
