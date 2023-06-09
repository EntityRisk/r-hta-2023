# Example R code for building decision models for health technology assessment

#' Create an example 3x3 transition probability matrix.
#'
#' @return A n_states by n_states matrix where n_states is the number of health
#' states.
trans_prob_matrix <- function() {
  matrix(
    c(
      0.8, 0.1, 0.1,
      0.0, 0.5, 0.5,
      0.0, 0.0, 1.0
    ),
    byrow = TRUE,
    nrow = 3
  )
}


#' Simulate disease progression with a Markov model.
#'
#' @param trans_probs A matrix containing probabilities of transitions between
#' health states.
#' @param n_cycles The number of cycles to simulate the model for. Default is
#' 5.
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


#' Compute discounted quality-adjusted life-years (QALYs).
#'
#' @param state_probs An n_cycles + 1 by n_states matrix containing state
#' occupancy probabilities.
#' @param qol A length n_states vector containing quality-of-life (QoL) weights
#' for each health state.
#' @param discount_rate Discount rate for QALYs.
compute_qalys <- function(state_probs, qol, discount_rate = 0.03) {
  qalys <- state_probs %*% qol
  n_years <- nrow(state_probs) # Assume each cycle is a year
  times <- seq(0, n_years - 1, by = 1) # Range is from [state, stop]
  discounted_qalys <- qalys / (1 + discount_rate)^times
  discounted_qalys
}
