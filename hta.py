"""Example Python code for building decision models for health technology
assessment."""

import numpy as np


def trans_prob_matrix():
    """Create an example 3x3 transition probability matrix."""

    return np.array([[0.8, 0.1, 0.1], [0.0, 0.5, 0.5], [1.0, 0.0, 0.0]])


if __name__ == "__main__":
    print(trans_prob_matrix())
