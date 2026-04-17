import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import rootfinding as rf
# a
def plot_water_tank_data(data_file_path):
    fig, ax = plt.subplots()
    data = pd.read_csv(data_file_path)
    height = data['Height'].values
    velocity = data['Velocity'].values
    ax.plot(height, velocity)
    ax.set_title("Water Velocity vs Water Height in Tank")
    ax.set_xlabel("Height [m]")
    ax.set_ylabel("Velocity [m/s]")

    return fig, ax

# b
def water_height_required(velocity):
    g = 9.81
    L = 5
    def f(h):
        return np.sqrt(2 * g * h) * np.tanh((2 / L) * np.sqrt(2 * g * h)) - velocity
    h0 = 0.5
    h1 = 3
    height, count = rf.secant(f, h0, h1, iterMax = 200)
    return height