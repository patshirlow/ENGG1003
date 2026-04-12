import numpy as np
import numbers
from collections.abc import Iterable

# To students reading this file. Do not use these variables in your solutions.
# These are part of what your functions should compute. Your functions are
# expected to work on more than just this data though.
q3_line_data = [
    "2.5, 0.0",
    "1.81, 60.0",
    "1.11, 120.0",
    "2.36, 180.0",
    "3.89, 240.0",
    "5.0, 300.0",
    "3.92, 360.0",
    "1.67, 420.0",
    "4.0, 480.0",
    "5.0, 540.0",
    "3.54, 600.0",
    "2.33, 660.0",
    "0.79, 720.0",
    "0.79, 780.0",
    "3.17, 840.0",
    "5.21, 900.0",
    "3.75, 960.0",
    "8.75, 1020.0",
    "8.89, 1080.0",
    "1.83, 1140.0",
    "0.9, 1200.0",
    "3.17, 1260.0",
    "3.75, 1320.0",
    "2.08, 1380.0",
    "2.71, 1440.0",
    "3.33, 1500.0",
]

runner_vel = np.array(
    [
        2.5,
        1.81,
        1.11,
        2.36,
        3.89,
        5.0,
        3.92,
        1.67,
        4.0,
        5.0,
        3.54,
        2.33,
        0.79,
        0.79,
        3.17,
        5.21,
        3.75,
        8.75,
        8.89,
        1.83,
        0.9,
        3.17,
        3.75,
        2.08,
        2.71,
        3.33,
    ]
)

t = np.array(
    [
        0.0,
        60.0,
        120.0,
        180.0,
        240.0,
        300.0,
        360.0,
        420.0,
        480.0,
        540.0,
        600.0,
        660.0,
        720.0,
        780.0,
        840.0,
        900.0,
        960.0,
        1020.0,
        1080.0,
        1140.0,
        1200.0,
        1260.0,
        1320.0,
        1380.0,
        1440.0,
        1500.0,
    ]
)


def q1_numeric_integration_close(result):
    """
    This function is used purely to indicate that the solution is somewhat
    close to the correct answer. It is provided to students, but markers will
    also be checking a much closer tolerance than what this function checks. So
    students should think about how best to check the answer is exactly correct
    """
    if not isinstance(result, numbers.Number):
        return {
            "passed": False,
            "expected": "The return value should be a number. Got : {type(result)}",
        }

    if result > 0.01:  # pyright: ignore
        return {
            "passed": False,
            "expected": "The numeric integration should be somewhat close to the exact result. Expected at least less than 1. Got : {result}",
        }
    return {
        "passed": True,
        "expected": "Got the right value!",
    }


def check_q2_plot_title(fig_ax_tup):
    try:
        _, ax = fig_ax_tup
        if isinstance(ax, Iterable):
            return {
                "passed": False,
                "expected": "There should only be one axes, make sure you are only creating one plot.",
            }
        if ax.get_title() == "Water Velocity vs Water Height in Tank":
            return {"passed": True, "expected": "Title matches the specification"}

        return {
            "passed": False,
            "expected": f"Title should be 'Water Velocity vs Water Height in Tank', got '{ax.get_title()}'",
        }

    except Exception as e:
        return {
            "passed": False,
            "expected": f"Failed to get axes title: {str(e)}. Make sure you are returning (fig, ax)",
        }


def check_q3_plot_title(fig_ax_tup):
    try:
        _, ax = fig_ax_tup
        if isinstance(ax, Iterable):
            return {
                "passed": False,
                "expected": "There should only be one axes, make sure you are only creating one plot.",
            }
        if ax.get_title() == "Run Velocity vs Time":
            return {"passed": True, "expected": "The title to match the figure"}

        return {"passed": False, "expected": "The title to match the figure"}

    except Exception as _:
        return {
            "passed": False,
            "expected": "Failed to get axes title. Make sure that you are returning (fig, ax)",
        }


UNIT_TESTS = [
    # Question 1
    # a) i)
    {
        "question": "Q1",
        "function_name": "trapezoidal_vs_polynomial",
        "input": [],
        "expected": q1_numeric_integration_close,
        "mark": 0.5,
        "feedback": "The numeric integration should be close (within 0.01 atleast) of the analytical solution",
    },
    {
        "question": "Q1",
        "function_name": "simpson_vs_polynomial",
        "input": [],
        "expected": q1_numeric_integration_close,
        "mark": 0.5,
        "feedback": "The numeric integration should be close (within 0.01 atleast) of the analytical solution",
    },
    # a) ii)
    {
        "question": "Q1",
        "function_name": "trapezoidal_vs_hyperbola",
        "input": [],
        "expected": q1_numeric_integration_close,
        "mark": 0.5,
        "feedback": "The numeric integration should be close (within 0.01 atleast) of the analytical solution",
    },
    {
        "question": "Q1",
        "function_name": "simpson_vs_hyperbola",
        "input": [],
        "expected": q1_numeric_integration_close,
        "mark": 0.5,
        "feedback": "The numeric integration should be close (within 0.01 atleast) of the analytical solution",
    },
    # a) iii)
    {
        "question": "Q1",
        "function_name": "trapezoidal_vs_sqrt",
        "input": [],
        "expected": q1_numeric_integration_close,
        "mark": 0.5,
        "feedback": "The numeric integration should be close (within 0.01 atleast) of the analytical solution",
    },
    {
        "question": "Q1",
        "function_name": "simpson_vs_sqrt",
        "input": [],
        "expected": q1_numeric_integration_close,
        "mark": 0.5,
        "feedback": "The numeric integration should be close (within 0.01 atleast) of the analytical solution",
    },
    # b) i)
    {
        "question": "Q1",
        "function_name": "numerical_std_normal",
        "input": [-1, 3],
        "expected": 0.83999,
        "float_tolerance": 1e-5,
        "mark": 1,
        "feedback": "The result should be very close to the analytical solution",
    },
    # b) ii)
    {
        "question": "Q1",
        "function_name": "random_std_normal",
        "input": [-1, 3],
        "expected": 0.839772,
        "float_tolerance": 1e-2,
        "mark": 1,
        "feedback": "The result will not be exact, but should be very close",
    },
    # Question 2
    # a)
    {
        "question": "Q2",
        "function_name": "plot_water_tank_data",
        "input": ["levels.csv"],
        "expected": check_q2_plot_title,
        "mark": 1,
        "feedback": "Make sure the title is set to 'Water Velocity vs Water Height in Tank'",
    },
    # b)
    {
        "question": "Q2",
        "function_name": "water_height_required",
        "input": [4.0],
        "expected": 0.929895777139532,
        "float_tolerance": 1e-2,
        "mark": 0.5,
        "feedback": "Test with velocity = 4.0",
    },
    # Question 3
    # a)
    {
        "question": "Q3",
        "function_name": "load_running_data",
        "input": ["running_data.txt"],
        "expected": q3_line_data,
        "mark": 2,
        "feedback": "Make sure that you have placed running_data.txt within the same directory as your Q3.py file",
    },
    # b)
    {
        "question": "Q3",
        "function_name": "parse_lines",
        "input": [["1, 2", "2, 4", "3, 6"]],
        "expected": (np.array([2, 4, 6]), np.array([1, 2, 3])),
        "mark": 1,
        "feedback": "Ensure you are splitting on the correct values",
    },
    # c)
    {
        "question": "Q3",
        "function_name": "max_velocity",
        "input": [np.array([1, 2, 3])],
        "expected": 3,
        "mark": 0.5,
    },
    {
        "question": "Q3",
        "function_name": "max_velocity",
        "input": [np.array([0, -1, 10])],
        "expected": ValueError("The runner should never run backwards"),
        "mark": 1,
    },
    # d)
    {
        "question": "Q3",
        "function_name": "min_velocity",
        "input": [np.array([4, 5, 1, 2, 3])],
        "expected": 1,
        "mark": 0.5,
    },
    # e)
    {
        "question": "Q3",
        "function_name": "average_velocity",
        "input": [np.array([1, 2, 3, 4, 5])],
        "expected": 3,
        "mark": 0.5,
    },
    # f)
    {
        "question": "Q3",
        "function_name": "velocity_interp",
        "input": [np.array([0, 1, 2]), np.array([10, 20, 30]), 1.5],
        "expected": 25,
        "mark": 0.5,
    },
    # g)
    {
        "question": "Q3",
        "function_name": "compute_trend",
        "input": [np.array([1, 2, 3]), np.array([0, -1, -2])],
        "expected": (-1, 1),
        "float_tolerance": 1e-5,
        "mark": 1,
        "feedback": "This is a y = -x + 1",
    },
    # h)
    {
        "question": "Q3",
        "function_name": "plot_run",
        "input": [t, runner_vel],
        "expected": check_q3_plot_title,
        "mark": 1,
        "feedback": "Make sure the title is set exactly as depicted",
    },
]
