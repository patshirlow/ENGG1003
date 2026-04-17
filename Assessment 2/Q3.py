import pandas as pd
import numpy as np

# a
def load_running_data(file_path):
    file_lines = []
    with open(file_path, "r") as f:
        for line in f:
            file_lines.append(line.strip())
    return file_lines
