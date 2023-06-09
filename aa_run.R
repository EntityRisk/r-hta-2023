# Run analyses with R

# R ----------------------------------------------------------------------------
source("functions.R")
trans_probs <- trans_probs_matrix()
state_probs <- sim_markov(trans_probs, n_cycles = 5)

print(trans_probs)
print(state_probs)
