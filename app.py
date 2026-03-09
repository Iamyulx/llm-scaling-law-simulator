import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("LLM Scaling Law Simulator (Chinchilla Inspired)")

# sliders
params = st.slider(
    "Model Parameters (billions)",
    0.1, 200.0, 10.0
)

tokens = st.slider(
    "Training Tokens (billions)",
    1.0, 2000.0, 300.0
)

compute = 6 * params * tokens

# scaling law constants
alpha = 0.34
beta = 0.28

a = 400
b = 410
L_inf = 1.7

# loss calculation
loss = L_inf + a/(params**alpha) + b/(tokens**beta)

st.write("Estimated Loss:", loss)
st.write("Estimated Compute:", compute)

# compute optimal tokens (Chinchilla rule approx)
optimal_tokens = 20 * params

st.write("Compute Optimal Tokens:", optimal_tokens)

if tokens < optimal_tokens:
    st.warning("Model is undertrained (needs more tokens)")

elif tokens > optimal_tokens:
    st.warning("Model is overtrained (too many tokens for size)")

else:
    st.success("Near compute-optimal training")

# plot scaling curve
param_range = np.linspace(0.1,200,200)

loss_curve = L_inf + a/(param_range**alpha) + b/(tokens**beta)

fig, ax = plt.subplots()

ax.plot(param_range, loss_curve)
ax.scatter([params],[loss])

ax.set_xlabel("Parameters (B)")
ax.set_ylabel("Loss")
ax.set_title("Scaling Curve")

st.pyplot(fig)
