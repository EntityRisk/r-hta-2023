"""Run analyses with Python."""

import functions as hta


def run_deterministic():
    """Run the deterministic model."""
    trans_probs = hta.trans_prob_matrix()
    state_probs = hta.sim_markov(trans_probs, n_cycles=5)
    discounted_qalys = hta.compute_qalys(state_probs, qol=[0.8, 0.6, 0])

    print(trans_probs)
    print(state_probs)
    print(discounted_qalys)


def run_psa():
    """Run the probabilistic sensitivity analysis."""
    sample_size = 100
    trans_data = (hta.trans_prob_matrix() * sample_size).astype(int)
    trans_probs_psa = hta.simulate_trans_probs(trans_data, n_sims=3)
    state_probs_psa = hta.sim_markov_psa(trans_probs_psa, n_cycles=5)

    print(state_probs_psa)
    state_probs_psa = hta.label_state_probs(state_probs_psa)
    print(state_probs_psa)
    print(state_probs_psa.mean(dim="sim"))


if __name__ == "__main__":
    run_deterministic()
    run_psa()
