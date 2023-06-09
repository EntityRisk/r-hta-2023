# Example R code for building decision models for health technology assessment

#' Create an example 3x3 transition probability matrix.
#'
#' @return A n_states by n_states matrix where n_states is the number of health
#' states.
trans_probs_matrix <- function() {
  matrix(
    c(
      0.8, 0.1, 0.1,
      0.0, 0.5, 0.5,
      1.0, 0.0, 0.0
    ),
    byrow = TRUE,
    nrow = 3
  )
}

#' Simulate disease progression with a Markov model.
#'
#' @param trans_probs A marix containing probabilities of transitions between
#' health states.
#' @param n_cycles The number of cycles to simulate the model for. Default is
#' 10.
#'
#' @return A n_cycles + 1 by n_states matrix storing state occupancy
#' probabilities by model cycle.
sim_markov <- function(trans_probs, n_cycles = 5) {
  state_probs <- matrix(NA, nrow = n_cycles + 1, ncol = 3) # The Markov trace
  state_probs[1, ] <- c(1, 0, 0) # Everyone starts in the same health state
  for (t in 1:n_cycles) { # R indexing starts at 1
    state_probs[t + 1, ] <- state_probs[t, ] %*% trans_probs
  }
  state_probs
}
