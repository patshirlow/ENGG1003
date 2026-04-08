import numpy as np
import matplotlib.pyplot as plt

# Data
t = np.linspace(-2, 2, 100)
f_values = t**2
g_values = np.exp(t)

# Create a figure with 2 rows and 1 column of subplots
fig, axes = plt.subplots(2, 1, figsize=(8, 6))

# --- Subplot 1: t^2 ---
axes[0].plot(t, f_values, 'r')
axes[0].set_title('Function: t^2')
axes[0].set_xlabel('t')
axes[0].set_ylabel('t^2')
axes[0].grid(True)

# --- Subplot 2: e^t ---
axes[1].plot(t, g_values, 'b--')
axes[1].set_title('Function: e^t')
axes[1].set_xlabel('t')
axes[1].set_ylabel('e^t')
axes[1].grid(True)

# Adjust layout so titles/labels don’t overlap
plt.tight_layout()
plt.show()