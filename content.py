"""
content.py - Entertainment and Information Content Module
Nexbridge Technologies - Virtual AI Assistant (Mini Alexa)

Responsibilities:
- Maintain curated collections of motivational quotes (FR-06), jokes (FR-07), and facts (FR-08).
- Provide functions to retrieve random selections from each collection using Python's random module.

AI/ML Concept:
- Content Recommendation Analogy: Demonstrates how early recommendation systems
  and information retrieval modules sample from categorized content candidate pools.
- Stochastic Behavior: Using pseudo-random number generators (PRNG) to simulate non-deterministic
  conversational responses.
"""

import random

# Predefined list of motivational quotes (FR-06)
QUOTES = [
    '"The only way to do great work is to love what you do." - Steve Jobs',
    '"Intelligence is the ability to adapt to change." - Stephen Hawking',
    '"Sometimes it is the people no one can imagine anything of who do the things no one can imagine." - Alan Turing',
    '"The analytical engine weaves algebraical patterns just as the Jacquard loom weaves flowers and leaves." - Ada Lovelace',
    '"You don\'t have to be great to start, but you have to start to be great." - Zig Ziglar',
    '"The secret of getting ahead is getting started." - Mark Twain',
    '"It does not matter how slowly you go as long as you do not stop." - Confucius',
    '"Simplicity is prerequisite for reliability." - Edsger W. Dijkstra',
    '"First, solve the problem. Then, write the code." - John Johnson',
    '"Code is like humor. When you have to explain it, it is bad." - Cory House',
    '"Continuous improvement is better than delayed perfection." - Mark Twain',
    '"The best way to predict the future is to invent it." - Alan Kay',
]

# Predefined list of programming, tech, and AI jokes (FR-07)
JOKES = [
    "Why did the developer go broke? Because they used up all their cache.",
    "There are 10 types of people in the world: those who understand binary, and those who don't.",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the computer cold? It left its Windows open.",
    "How do you comfort a JavaScript bug? You console it.",
    "A SQL query walks into a bar, walks up to two tables and asks: 'Can I join you?'",
    "Why did the neural network cross the road? To optimize its loss function on the other side.",
    "What is a programmer's favorite hangout spot? The Foo Bar.",
    "Why was the machine learning model feeling insecure? It had too much bias.",
    "An optimist sees the glass half full. A pessimist sees it half empty. A programmer sees the glass twice as large as necessary.",
    "Why do Python programmers wear glasses? Because they don't C#!",
    "Real programmers count from 0.",
]

# Predefined list of computer science, AI, and science facts (FR-08)
FACTS = [
    "The first computer programmer in history was Ada Lovelace, who wrote an algorithm for the Analytical Engine in 1843.",
    "The term 'bug' in computing originated in 1947 when Grace Hopper found an actual moth trapped inside the Harvard Mark II relay.",
    "Python was named after the British comedy series 'Monty Python\'s Flying Circus', not after the snake.",
    "The concept of the Perceptron, the earliest artificial neural network model, was invented by Frank Rosenblatt in 1958.",
    "The Apollo 11 Lunar Module guidance computer operated with only 4 kilobytes of RAM and 72 kilobytes of ROM.",
    "The word 'robot' was coined by Czech writer Karel Capek in his 1920 play 'R.U.R.', derived from the Slavic word 'robota' meaning forced labor.",
    "Deep Blue became the first computer chess-playing system to defeat a reigning world chess champion (Garry Kasparov) in 1997.",
    "Over 85% of modern AI systems rely on gradient descent and backpropagation to learn from data.",
    "The ENIAC, built in 1945, weighed more than 27 tons and consumed about 150 kilowatts of electricity.",
    "Alan Turing proposed the 'Imitation Game' (Turing Test) in 1950 to evaluate whether a machine can exhibit human-equivalent intelligence.",
]


def get_random_quote() -> str:
    """
    Selects and formats a random motivational quote from the QUOTES pool.

    Returns:
        str: Assistant response containing the selected quote.
    """
    selected = random.choice(QUOTES)
    return f"Assistant: Here's a thought for you:\n  {selected}"


def get_random_joke() -> str:
    """
    Selects and formats a random joke from the JOKES pool.

    Returns:
        str: Assistant response containing the selected joke.
    """
    selected = random.choice(JOKES)
    return f"Assistant: {selected}"


def get_random_fact() -> str:
    """
    Selects and formats a random educational fact from the FACTS pool.

    Returns:
        str: Assistant response containing the selected fact.
    """
    selected = random.choice(FACTS)
    return f"Assistant: Did you know? {selected}"
