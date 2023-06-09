"""Run analyses with Python."""

import functions as hta

trans_probs = hta.trans_probs_matrix()
state_probs = hta.sim_markov(trans_probs, n_cycles=5)

print(trans_probs)
print(state_probs)
