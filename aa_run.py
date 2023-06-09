"""Run analyses with Python."""

import functions as hta

trans_probs = hta.trans_probs_matrix()
state_probs = hta.sim_markov(trans_probs, n_cycles=5)
discounted_qalys = hta.compute_qalys(state_probs, qol=[0.8, 0.6, 0])

print(trans_probs)
print(state_probs)
print(discounted_qalys)
