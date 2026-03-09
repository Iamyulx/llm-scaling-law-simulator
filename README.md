# llm-scaling-law-simulator
Interactive simulator for Large Language Model scaling laws inspired by the paper:  
Training Compute-Optimal Large Language Models Jordan Hoffmann et al. — DeepMind

This tool allows users to explore how model size, training data, and compute interact to determine performance.

The simulator demonstrates the core idea behind Chinchilla scaling laws: optimal training requires balancing model parameters and dataset size.



# Scaling Laws

Large Language Models follow predictable relationships between:

Model Parameters (N)

Training Tokens (D)

Compute Budget (C)

Loss

The loss can be approximated with a scaling law:

L(N, D) = L∞ + a/N^α + b/D^β

Where:

N = number of model parameters

D = number of training tokens

L∞ = irreducible loss

α, β = scaling exponents



# Chinchilla Compute-Optimal Rule

The Chinchilla paper showed that optimal performance occurs when:

Tokens ≈ 20 × Parameters

If the model violates this rule:

Too few tokens → undertrained model

Too many tokens → overtrained model



# Interactive Features

The simulator lets users:

Adjust model parameters

Adjust training tokens

Observe the estimated loss

Compute approximate training compute

Visualize the scaling curve

Detect undertraining or overtraining relative to Chinchilla scaling.



# Example Output

The simulator generates a scaling curve like this:

Parameters vs Loss

with the selected configuration highlighted.



# Run the App

Clone the repository:

git clone https://github.com/yourusername/llm-scaling-law-simulator
cd llm-scaling-law-simulator

Install dependencies:

pip install -r requirements.txt

Run the app:

streamlit run app.py


# Why This Project Matters

Understanding scaling laws is essential for designing modern AI systems.

Scaling laws influenced the training of models such as:

GPT series

PaLM

DeepMind Gemini

This simulator provides intuition about how model size and dataset size interact in large-scale training.
