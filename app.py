import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# --- System Configuration ---
st.set_page_config(page_title="Industrial Stochastic Simulator", layout="wide")
st.title("🧪 Resourceful Kinetic Utility (v2.0.0)")
st.markdown("Professional-grade stochastic engine for molecular simulation.")

# --- Sidebar Controls (Path A) ---
st.sidebar.header("Input Parameters")
k = st.sidebar.slider("Reaction Rate Constant (k)", 0.0, 2.0, 0.5)
n_init = st.sidebar.number_input("Initial Molecular Count", 10, 5000, 500)
t_max = st.sidebar.slider("Max Simulation Time (s)", 10, 500, 100)

# --- The Logic (Path B) ---
if st.button("Execute Simulation"):
    # Safety Valve
    if k <= 0:
        st.error("Market-Safety Alert: Rate constant (k) must be greater than 0 to proceed.")
    else:
        # Initialize simulation
        t = [0.0]
        n = [n_init]
        
        # Stochastic Loop
        while n[-1] > 0 and t[-1] < t_max:
            propensity = k * n[-1]
            dt = -np.log(np.random.random()) / propensity
            t.append(t[-1] + dt)
            n.append(n[-1] - 1)

        # Visualization
        fig, ax = plt.subplots(figsize=(10, 4))
        ax.step(t, n, where='post', color='#00FFAA', linewidth=2)
        ax.set_xlabel("Time (s)")
        ax.set_ylabel("Molecular Quantity")
        ax.set_title("Stochastic Decay Profile (A -> Product)")
        ax.grid(True, alpha=0.2)
        
        st.pyplot(fig)
        st.success(f"Execution Successful: {len(n)-1} molecular events tracked.")