"""Example Python code for building decision models for health technology
assessment."""

import numpy as np


def trans_probs_matrix():
    """Create an example 3x3 transition probability matrix.

    Returns
    -------
    numpy.ndarray
        An n_states by n_states array where n_states is the number of
        health states.
    """
    return np.array([[0.8, 0.1, 0.1], [0.0, 0.5, 0.5], [1.0, 0.0, 0.0]])


def sim_markov(trans_probs, n_cycles=5):
    """Simulate disease progression with a Markov model.

    Parameters
    ----------
    trans_probs : numpy.ndarray
        A 2D numpy array containing probabilities of transition between health
        states.
    n_cycles : int, default=10
        The number of cycles to simulate the model for. Default is 10.

    Returns
    -------
    numpy.ndarray
        A n_cycles + 1 by n_states array storing state occupancy probabilities
        by model cycle.
    """
    state_probs = np.empty((n_cycles + 1, 3))  # The Markov trace
    state_probs[0, :] = [1, 0, 0]  # Everyone starts in the same state
    for t in range(n_cycles):  # Python indexing starts at 0
        state_probs[t + 1, :] = state_probs[t, :] @ trans_probs
    return state_probs
