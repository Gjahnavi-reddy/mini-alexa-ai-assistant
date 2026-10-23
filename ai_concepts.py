"""
ai_concepts.py - Educational AI, Machine Learning, and Deep Learning Demonstrations
Nexbridge Technologies - Virtual AI Assistant (Mini Alexa)

Responsibilities:
- Demonstrate Rule-Based Systems & Decision Tree Logic via time-of-day activity recommendations (FR-13).
- Demonstrate Artificial Neurons, Perceptron Architecture, and Forward Propagation using pure Python arithmetic (FR-14).
- Provide clear analogies connecting beginner code to foundational AI/ML/DL concepts.

Concepts Covered:
- Rule-Based Systems & Decision Trees (AI & ML).
- Artificial Neurons, Weights, Bias, Activation Function, and Forward Propagation (DL).
"""

from typing import List, Dict, Any, Optional
from datetime_utils import get_current_hour


# =====================================================================
# PART 1: RULE-BASED SYSTEM & DECISION TREE DEMO (FR-13)
# =====================================================================

def recommend_activity(hour: Optional[int] = None) -> str:
    """
    Recommends a suitable activity based on the hour of the day (0-23).
    Demonstrates an explicit Rule-Based Decision System (and Decision Tree logic).

    In traditional AI, expert systems rely on developer-engineered rules
    (if/elif/else conditions) rather than learning weights from data.

    Decision Tree Architecture:
                [ Is hour < 5 or >= 23 ? ]
                      /              \\
                   YES                NO
               (Sleep/Rest)     [ Is hour < 9 ? ]
                                   /          \\
                                 YES           NO
                             (Morning)    [ Is hour < 12 ? ]
                                             /          \\
                                           YES           NO
                                       (Deep Work)    [ Is hour < 14 ? ]
                                                         /          \\
                                                       YES           NO
                                                    (Lunch)     [ ... ]

    Args:
        hour: Optional integer (0-23). If None, uses current system hour.

    Returns:
        str: Assistant recommendation and rule explanation.
    """
    if hour is None:
        hour = get_current_hour()

    # Rule evaluation using explicit conditional branches
    if 5 <= hour < 9:
        period = "Early Morning"
        activity = "Morning routine, stretching, and a healthy breakfast."
        focus = "Set clear goals for the day ahead."
    elif 9 <= hour < 12:
        period = "Mid Morning"
        activity = "Deep work, coding challenges, and logic building."
        focus = "Peak cognitive focus window - tackle the hardest task first!"
    elif 12 <= hour < 14:
        period = "Afternoon Lunch"
        activity = "Lunch break, hydration, and stepping away from screens."
        focus = "Recharge your mental energy."
    elif 14 <= hour < 18:
        period = "Mid Afternoon"
        activity = "Collaborative projects, code reviews, and learning new AI concepts."
        focus = "Great time for practical application and team syncs."
    elif 18 <= hour < 21:
        period = "Evening"
        activity = "Dinner, physical exercise, or light personal reading."
        focus = "Decompress from daily engineering work."
    elif 21 <= hour < 23:
        period = "Late Evening"
        activity = "Journaling, reviewing daily wins, and winding down."
        focus = "Prepare your mind for restful sleep."
    else:  # 23, 0, 1, 2, 3, 4
        period = "Night / Sleep Window"
        activity = "Deep sleep and physical rest."
        focus = "Rest is critical for memory consolidation and cognitive performance."

    time_str = f"{hour:02d}:00"
    explanation = (
        f"Assistant: [Rule-Based AI Recommendation]\n"
        f"  * Current Time Reference: {time_str} ({period})\n"
        f"  * Recommended Activity: {activity}\n"
        f"  * Cognitive Focus: {focus}\n\n"
        f"  [AI Concept Note]: This feature simulates a Rule-Based Expert System.\n"
        f"  It maps input feature 'hour={hour}' to an output class using an explicit\n"
        f"  deterministic decision tree with if-elif conditions."
    )
    return explanation


# =====================================================================
# PART 2: ARTIFICIAL NEURON & PERCEPTRON SIMULATION (FR-14)
# =====================================================================

def step_activation(z: float, threshold: float = 0.0) -> int:
    """
    A mathematical Step Activation Function (Heaviside step function).
    Maps any continuous real-valued sum to a binary decision {0, 1}.

    Formula:
        f(z) = 1 if z >= threshold else 0
    """
    return 1 if z >= threshold else 0


def calculate_perceptron(
    inputs: List[float],
    weights: List[float],
    bias: float,
    threshold: float = 0.0
) -> Dict[str, Any]:
    """
    Simulates a single Artificial Neuron (Perceptron) forward calculation.

    Mathematical Model:
        z = (x1 * w1) + (x2 * w2) + ... + (xn * wn) + bias
        output = step_activation(z)

    Analogies:
        - Inputs (x): Observable features / sensor readings.
        - Weights (w): Importance or strength of each feature.
        - Bias (b): Base threshold / baseline tendency of the neuron to activate.
        - Weighted Sum (z): Net accumulation of incoming stimuli.
        - Activation Function: Non-linear gate deciding if the neuron 'fires'.
        - Forward Propagation: The left-to-right flow from inputs to final output.

    Args:
        inputs: List of input feature values [x1, x2, ...].
        weights: List of synaptic weights [w1, w2, ...].
        bias: Threshold shift parameter (b).
        threshold: Activation threshold (default: 0.0).

    Returns:
        Dict with step-by-step arithmetic details.
    """
    if len(inputs) != len(weights):
        raise ValueError("Number of inputs must equal number of weights.")

    # Calculate weighted products for each input
    products = [x * w for x, w in zip(inputs, weights)]
    dot_product = sum(products)
    weighted_sum = dot_product + bias
    activation_output = step_activation(weighted_sum, threshold=threshold)

    return {
        "inputs": inputs,
        "weights": weights,
        "bias": bias,
        "products": products,
        "dot_product": dot_product,
        "weighted_sum": weighted_sum,
        "output": activation_output,
    }


def multi_layer_forward_demo(x1: float, x2: float) -> str:
    """
    Demonstrates Forward Propagation through a minimal 2-layer Neural Network
    (Hidden Layer -> Output Layer) without any training libraries.

    Layer 1 (Hidden Layer - 2 Neurons):
        Neuron H1: Detects pattern A
        Neuron H2: Detects pattern B

    Layer 2 (Output Neuron):
        Combines activations of H1 and H2.
    """
    # Hidden Neuron 1
    h1 = calculate_perceptron(inputs=[x1, x2], weights=[0.5, 0.5], bias=-0.4)
    # Hidden Neuron 2
    h2 = calculate_perceptron(inputs=[x1, x2], weights=[-0.5, 0.8], bias=-0.1)

    # Output Neuron receiving activations of H1 and H2
    out = calculate_perceptron(inputs=[float(h1["output"]), float(h2["output"])], weights=[0.7, 0.6], bias=-0.5)

    report = (
        f"  --- Forward Propagation Walkthrough ---\n"
        f"  Input Layer:           [x1 = {x1}, x2 = {x2}]\n"
        f"  Hidden Neuron 1:       z1 = {h1['weighted_sum']:.2f} -> Activation = {h1['output']}\n"
        f"  Hidden Neuron 2:       z2 = {h2['weighted_sum']:.2f} -> Activation = {h2['output']}\n"
        f"  Output Layer Neuron:   z_out = {out['weighted_sum']:.2f} -> Final Output = {out['output']}\n"
        f"  Result Interpretation: {'Activated (Class 1)' if out['output'] == 1 else 'Not Activated (Class 0)'}"
    )
    return report


def run_perceptron_interactive(user_name: str = "Friend") -> None:
    """
    Interactive command-line demonstration of Perceptron forward propagation (FR-14).
    Provides educational context and real-world analogy walkthroughs.
    """
    print(f"\n=======================================================")
    print(f"   ARTIFICIAL NEURON (PERCEPTRON) DEMO - Deep Learning")
    print(f"=======================================================")
    print(
        "A Perceptron is the fundamental building block of Artificial Neural Networks,\n"
        "invented by Frank Rosenblatt in 1958. It computes a weighted sum of its inputs,\n"
        "adds a bias, and passes the sum through an activation function.\n"
    )
    print("ASCII Neural Diagram:")
    print("  Inputs (x)          Weights (w)")
    print("  [ x1 ] ----------( w1 = +0.4 )---------\\ ")
    print("                                          +--> [ Sum: (w*x) + b ] --> [ Step Function ] --> Output (0 or 1)")
    print("  [ x2 ] ----------( w2 = +0.03 )--------/ ")
    print("  [ Bias ] --------(  b = -2.5  )-------/ ")
    print()
    print("Choose a demonstration mode:")
    print("  1. Student Exam Predictor (Real-World Classification Analogy)")
    print("  2. Custom Perceptron Calculation (Enter your own inputs, weights, bias)")
    print("  3. Hidden Layer Demonstration (2-Layer Neural Network Forward Pass)")
    print("  4. Return to main assistant")

    try:
        choice = input(f"\n[{user_name}] Enter option (1-4): ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\nReturning to assistant.")
        return

    if choice == "1":
        print(f"\n--- Scenario: Predicting if an Intern Passes the AI Milestone Test ---")
        print("We use 2 observable features:")
        print("  Feature x1: Weekly Study Hours (e.g., 1 to 10)")
        print("  Feature x2: Lecture Attendance Percentage (0 to 100)")
        print("Fixed Learned Parameters:")
        print("  Weight w1: 0.40  (Each hour of study adds +0.40 to decision score)")
        print("  Weight w2: 0.03  (Each % attendance adds +0.03 to decision score)")
        print("  Bias b:   -2.50  (Threshold barrier: must overcome -2.50 to pass)\n")

        try:
            raw_hours = input("Enter estimated study hours per week (e.g., 5): ").strip()
            x1 = float(raw_hours)
            raw_att = input("Enter lecture attendance % (e.g., 80): ").strip()
            x2 = float(raw_att)
        except ValueError:
            print("Assistant: Invalid numeric input. Returning to assistant.")
            return

        w1, w2, bias = 0.40, 0.03, -2.50
        result = calculate_perceptron(inputs=[x1, x2], weights=[w1, w2], bias=bias)

        print("\n--- Forward Propagation Steps ---")
        print(f"1. Input Vector:         X = [{x1}, {x2}]")
        print(f"2. Weight Vector:        W = [{w1}, {w2}]")
        print(f"3. Weighted Products:    (x1 * w1) = {result['products'][0]:.2f}, (x2 * w2) = {result['products'][1]:.2f}")
        print(f"4. Dot Product Sum:      {result['dot_product']:.2f}")
        print(f"5. Add Bias ({bias}):    Net Score z = {result['weighted_sum']:.2f}")
        print(f"6. Step Activation:      f(z) = 1 if z >= 0 else 0")
        print(f"7. Output Value:         {result['output']}")
        print(f"\nPrediction Outcome:")
        if result['output'] == 1:
            print(f"[PASS] The neuron activated (Output = 1). The intern is predicted to pass the milestone!")
        else:
            print(f"[NEEDS PREPARATION] (Output = 0). Net score did not overcome the bias threshold.")

    elif choice == "2":
        print("\n--- Custom Perceptron Experiment ---")
        try:
            x1 = float(input("Enter Input x1 (float): ").strip())
            w1 = float(input("Enter Weight w1 (float): ").strip())
            x2 = float(input("Enter Input x2 (float): ").strip())
            w2 = float(input("Enter Weight w2 (float): ").strip())
            b = float(input("Enter Bias b (float): ").strip())
        except ValueError:
            print("Assistant: Invalid input. Must be numbers.")
            return

        res = calculate_perceptron([x1, x2], [w1, w2], b)
        print(f"\nCalculation Result:")
        print(f"  Weighted Sum (z): {res['weighted_sum']:.4f}")
        print(f"  Step Activation (z >= 0): {res['output']}")

    elif choice == "3":
        print("\n--- Hidden Layer & Multi-Neuron Network Demo ---")
        print("Passing inputs through a 2-layer Neural Network:")
        try:
            x1 = float(input("Enter Input Feature x1 (e.g. 1.0): ").strip())
            x2 = float(input("Enter Input Feature x2 (e.g. 0.5): ").strip())
        except ValueError:
            print("Assistant: Invalid input. Defaulting to x1=1.0, x2=0.5")
            x1, x2 = 1.0, 0.5

        report = multi_layer_forward_demo(x1, x2)
        print(report)

    else:
        print("Returning to main assistant loop.")
