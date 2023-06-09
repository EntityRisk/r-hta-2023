"""Run analyses with Python."""

import functions as hta

# Deterministic analysis
trans_probs = hta.trans_probs_matrix()
state_probs = hta.sim_markov(trans_probs, n_cycles=5)
discounted_qalys = hta.compute_qalys(state_probs, qol=[0.8, 0.6, 0])

print(trans_probs)
print(state_probs)
print(discounted_qalys)

# Probabilistic sensitivity analysis
SAMPLE_SIZE = 100
trans_data = (trans_probs * SAMPLE_SIZE).astype(int)
trans_probs_psa = hta.simulate_trans_probs(trans_data, n_sims=3)
state_probs_psa = hta.sim_markov_psa(trans_probs_psa, n_cycles=5)
