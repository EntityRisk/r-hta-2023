# Run analyses with R

source("functions.R")
trans_probs <- trans_prob_matrix()
state_probs <- sim_markov(trans_probs, n_cycles = 5)
discounted_qalys <- compute_qalys(
  state_probs,
  qol = c(0.8, 0.6, 0)
)

print(trans_probs)
print(state_probs)
print(discounted_qalys)
