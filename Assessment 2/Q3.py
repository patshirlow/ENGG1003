import numpy as np
import scipy.optimize as sco
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

# a
def load_running_data(file_path):
    try:
        f = open(file_path, "r")
        lines = f.readlines()
        f.close()
        file_lines = []
        for line in lines:
            file_lines.append(line.strip())
        return file_lines
    except:
        return []
print(load_running_data("running_data.txt"))

# b
def parse_lines(file_lines):
    t_list = []
    velocity_list = []
    for line in file_lines:
        parts = line.split(",")
        v = float(parts[0].strip())
        t = float(parts[1].strip())
        velocity_list.append(v)
        t_list.append(t)
    t = np.array(t_list)
    velocity = np.array(velocity_list)
    return t, velocity
print(parse_lines(load_running_data("running_data.txt")))

# c
def max_velocity(velocities):
    velocities = np.array(velocities)
    if np.any(velocities < 0):
        raise ValueError("The runner should never run backwards")
    max_v = np.max(velocities)
    return max_v
print(max_velocity(parse_lines(load_running_data("running_data.txt"))))

# d
def min_velocity(velocities):
    velocities = np.array(velocities)
    if np.any(velocities < 0):
        raise ValueError("The runner should never run backwards")
    min_v = np.min(velocities)
    return min_v
print(min_velocity(parse_lines(load_running_data("running_data.txt"))))

# e

def average_velocity(velocities):
    velocities = np.array(velocities)
    if np.any(velocities < 0):
        raise ValueError("The runner should never run backwards")
    avg_v = np.mean(velocities)
    return avg_v
print(average_velocity(parse_lines(load_running_data("running_data.txt"))))

# f
def velocity_interp(time, velocity, time_to_interpolate):
    if time_to_interpolate < np.min(time) or time_to_interpolate > np.max(time):
        raise ValueError("Cannot interpolate outside of measurement time")
    f = interp1d(time, velocity)
    interpolated_velocity = float(f(time_to_interpolate))

    return interpolated_velocity

# g
def line(t, m, c):
    return m * t + c

def compute_trend(time, velocity):
    popt, _ = sco.curve_fit(line, time, velocity)
    m = popt[0]
    c = popt[1]
    return m, c

# h
def plot_run(time, velocity):
    fig, ax = plt.subplots()
    ax.plot(time, velocity, color='blue', label='Velocity')
    m, c = compute_trend(time, velocity)
    velocity_trend = m * time + c
    ax.plot(time, velocity_trend, color='orange', linestyle='--', label='Trend')
    ax.set_xlabel('Time [s]')
    ax.set_ylabel('Velocity [m/s]')
    ax.set_title('Run Velocity vs Time')
    ax.axis([0, 1500, 0, 10])
    ax.set_xticks(np.linspace(0, 1500, 16))
    ax.set_yticks(np.linspace(0, 10, 21))
    ax.grid(True)
    ax.legend()
    return fig, ax





