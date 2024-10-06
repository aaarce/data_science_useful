#cumulative distribution function (CDF) but using R to solve problem 3 exam 1 practice
# Given data
y_values <- c(0, 2, 4)    # Discrete values of Y
p_y <- c(0.1, 0.3, 0.6)   # Corresponding probabilities

# Step 1: Calculate Cumulative Distribution Function (CDF)
F_y <- cumsum(p_y)  # Cumulative sum of probabilities

# Step 2: Extend the CDF for values outside the range of Y
# We include extra points to account for the CDF before the first y-value and after the last y-value
y_ext <- c(-2, 0, 2, 4, 6)  # Extending the Y values range
F_y_ext <- c(0, 0.1, 0.4, 1, 1)  # CDF values for these points

# Step 3: Plot the CDF
plot(y_ext, F_y_ext, type="s", col="blue", main="Cumulative Distribution Function (CDF)",
     xlab="y", ylab="F(y)", ylim=c(0, 1.2), xlim=c(-2, 6))
grid()

# Step 4: Calculate Expected Value E(Y) and Variance Var(Y)
E_Y <- sum(y_values * p_y)  # E(Y) = sum of y * p(y)
E_Y_squared <- sum((y_values ^ 2) * p_y)  # E(Y^2) = sum of y^2 * p(y)
Var_Y <- E_Y_squared - E_Y^2  # Var(Y) = E(Y^2) - [E(Y)]^2

# Step 5: Output the results
cat("Expected Value E(Y):", E_Y, "\n")
cat("Variance Var(Y):", Var_Y, "\n")

