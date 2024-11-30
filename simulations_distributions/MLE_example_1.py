##HMWK 12 Max Likelihood Estimation: Calculate MLE for theta and theta^2 
### Problems 9-14
import numpy as np

# Step 1: Define datasets for Problems 9, 11, and 13 (ALL HERE)
problem_9_data = [2.85, 11.07, 3.84, 7.92, 5.83, 8.81, 12.33, 9.74, 3.38, 21.91]
problem_11_data = [17.47, 9.1, 13.74, 30.68, 41.66, 16.53, 43.44, 21.18, 43.16, 74.17]
problem_13_data = [0.7, 0.83, 2.39, 1.98, 3.76, 2.24, 12.44, 7.34, 2.76, 14.03]

# Problem 11-12
# Step 2: Function to calculate MLE for theta and theta^2
def calculate_theta_and_theta_squared(data):
    sum_data = np.sum(data)  # Sum of data
    n = len(data)  # Number of observations
    theta_hat = sum_data / (2 * n)  # MLE for theta
    theta_squared_hat = theta_hat**2  # MLE for theta^2
    return theta_hat, theta_squared_hat

# Step 3: Calculate for Problem 9
theta_9, theta_squared_9 = calculate_theta_and_theta_squared(problem_9_data)

# Step 4: Print results
print(f"Number of observations (n): {len(problem_9_data)}")
print(f"MLE for theta (θ): {theta_9}")##problem 9
print(f"MLE for theta (θ) squared: {theta_squared_9}")##problem 10

###Problems 11-12
import numpy as np

### Problem 11-12
problem_11_data = [17.47, 9.1, 13.74, 30.68, 41.66, 16.53, 43.44, 21.18, 43.16, 74.17]

# Known value of alpha
alpha = 3.7

# Step 1: Calculate MLE for theta
sum_data = np.sum(problem_11_data)  # Sum of all x_i
n = len(problem_11_data)  # Number of observations
theta_hat = sum_data / (n * alpha)  # MLE for theta

# Step 2: Calculate MLE for sqrt(theta)
sqrt_theta_hat = np.sqrt(theta_hat)

theta_hat, sqrt_theta_hat
print(f"#Number of observations (n): {len(problem_11_data)}")
print(f"MLE for theta (θ) (Prob 11): {theta_hat}")
print(f"MLE for theta (θ) squared (Prob 12): {sqrt_theta_hat}")##problem 10


### Problems 13-14
import numpy as np

# Data for Problem 13
problem_13_data = [0.7, 0.83, 2.39, 1.98, 3.76, 2.24, 12.44, 7.34, 2.76, 14.03]

# Step 1: Calculate X_max
X_max = max(problem_13_data)

# Step 2: Calculate MLE for theta
theta_hat = (X_max - 1) / 2 ##note, tbd if this formula is standard

# Step 3: Calculate MLE for Variance
variance_hat = ((2 * theta_hat + 1) ** 2) / 12 ##note, this seems to always be appropriate formula


# Results
print({X_max})
print(f"Num of Observations: {len(problem_13_data)}")
print(f"MLE for theta (θ) (Prob 13): {theta_hat}")
print(f"MLE of the variance of this distribution: {variance_hat}")
