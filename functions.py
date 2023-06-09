"""Example Python code for building decision models for health technology
assessment."""

import numpy as np
import xarray as xr


def trans_prob_matrix():
    """Create an example 3x3 transition probability matrix.

    Returns
    -------
    numpy.ndarray
        An n_states by n_states array where n_states is the number of
        health states.
    """
    return np.array([[0.8, 0.1, 0.1], [0.0, 0.5, 0.5], [0.0, 0.0, 1.0]])


def sim_markov(trans_probs, n_cycles=5):
    """Simulate disease progression with a Markov model.

    Parameters
    ----------
    trans_probs : numpy.ndarray
        A 2D numpy array containing probabilities of transition between health
        states.
    n_cycles : int, default=5
        The number of cycles to simulate the model for. Default is 5.

    Returns
    -------
    numpy.ndarray
        An n_cycles + 1 by n_states array storing state occupancy probabilities
        by model cycle.
    """
    state_probs = np.empty((n_cycles + 1, 3))  # The Markov trace
    state_probs[0, :] = [1, 0, 0]  # Everyone starts in the same state
    for t in range(n_cycles):  # Python indexing starts at 0
        state_probs[t + 1, :] = state_probs[t, :] @ trans_probs
    return state_probs


def compute_qalys(state_probs, qol, discount_rate=0.03):
    """Compute discounted quality-adjusted life-years (QALYs).

    Parameters
    ----------
    state_probs : numpy.ndarray
        An n_cycles + 1 by n_states array containing state occupancy
        probabilities.
    qol : list or numpy.ndarray
        A 1D array_like of length n_states containing quality-of-life (QoL)
        weights for each health state.
    discount_rate : float, default=0.03
        Discount rate for QALYs.
    """
    qalys = state_probs @ qol
    n_years = state_probs.shape[0]  # Assume each cycle is a year
    times = np.arange(0, n_years, step=1)  # Range is from [state, stop)
    discounted_qalys = qalys / (1 + discount_rate) ** times
    return discounted_qalys


def simulate_trans_probs(trans_data, n_sims=1000):
    """Simulate transition probabilities using a Dirichlet distribution for
    each starting health state.

    Parameters
    ----------
    trans_data : numpy.ndarray
        A 2D numpy array containing data on the number of transitions between
        heath states.
    n_sims : int, default=1000
        Number of parameter simulations. Default is 1000.

    Returns
    -------
    numpy.ndarray
        An n_sims by n_states by n_states 3D array.
    """
    row_1 = np.random.dirichlet(trans_data[0,], size=n_sims)
    row_2 = np.hstack(
        (  # Dirichlet can't have parameter <= 0, so add a column of 0's
            np.zeros((n_sims, 1)),
            np.random.dirichlet(trans_data[1, 1:], size=n_sims),
        )
    )
    row_3 = np.hstack(  # The 3rd health state is the death state
        (
            np.zeros((n_sims, 2)),  # No one is in the first 2 states
            np.ones((n_sims, 1)),  # Everyone has died
        )
    )
    return np.dstack((row_1, row_2, row_3))


def sim_markov_psa(trans_probs, n_cycles=5):
    """Simulate disease progression with a Markov model and use probabilistic
    sensitivity analysis (PSA) to propagate parameter uncertainty.

    Parameters
    ----------
    trans_probs : numpy.ndarray
        An n_sims by n_states by n_states 3D array where each slice is a
        transition probability matrix for a given draw from the PSA.
    n_cycles : int, default=5
        The number of cycles to simulate the model for. Default is 5.

    Returns
    -------
    numpy.ndarray
        An n_sims by n_cycles + 1 by n_states array storing state occupancy
        probabilities by model cycle.
    """
    n_sims = trans_probs.shape[0]  # First axis is the simulation axis
    state_probs = np.empty((n_sims, n_cycles + 1, 3))  # The Markov trace
    state_probs[:, 0, :] = [1, 0, 0]  # Everyone starts in the same state
    for t in range(n_cycles):  # Python indexing starts at 0
        state_probs[:, [t + 1], :] = state_probs[:, [t], :] @ trans_probs
    return state_probs


def label_state_probs(state_probs):
    """Convert state occupancy probabilities stored as a numpy array
    to a labeled xarray DataArray.

    Parameters
    ----------
    state_probs : numpy.ndarray
        An n_sims by n_cycles + 1 by n_states array storing state occupancy
        probabilities by model cycle.

    Returns
    -------
    xarray.DataArray
        State occupancy probabilities stored in an array with dimensions
        "sim", "time", and "state", indexing parameter simulations from the
        PSA, model time (in years), and the health state, respectively.
    """
    return xr.DataArray(
        state_probs,
        dims=["sim", "time", "state"],
        coords={  # We assumed each cycle is a year
            "sim": range(state_probs.shape[0]),
            "time": range(state_probs.shape[1]),
            "state": ["Sick", "Sicker", "Death"],
        },
    )
