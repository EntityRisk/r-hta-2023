# Example R code for building decision models for health technology assessment

#' Create an example 3x3 transition probability matrix.
trans_prob_matrix <- function() {
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

# Run the functions-------------------------------------------------------------
print(trans_prob_matrix())
