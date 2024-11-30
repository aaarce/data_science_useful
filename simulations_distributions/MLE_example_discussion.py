##HmWK 12 - Problems 2-7 up for discussion
import numpy as np
import matplotlib.pyplot as plt

# Example data (replace with your dataset & note none provided in generic problem)
data = [4.5, 5.0, 6.1, 5.8, 4.9, 5.2]

# Step 1: Calculate MLE for mu and sigma^2
mu_hat = np.mean(data)
sigma_squared_hat = np.mean((np.array(data) - mu_hat)**2)

# Step 2: Calculate unbiased estimator for sigma^2
n = len(data)
unbiased_sigma_squared = (n / (n - 1)) * sigma_squared_hat


# Step 3: Simulate distribution of mu_hat 
num_simulations = 10000
sample_means = []
for _ in range(num_simulations):
    sample = np.random.normal(loc=mu_hat, scale=np.sqrt(unbiased_sigma_squared), size=n)
    sample_means.append(np.mean(sample))

# Plot the distribution of mu_hat
plt.hist(sample_means, bins=30, density=True, alpha=0.6, label="Simulated Distribution")
plt.title("Sampling Distribution of $\hat{\mu}$")
plt.xlabel("$\hat{\mu}$")
plt.ylabel("Density")
plt.legend()
plt.show()

# Step 4: Simulate Chi-Squared distribution for (n-1)*sigma^2/sigma^2
chi_squared_values = []
for _ in range(num_simulations):
    sample = np.random.normal(loc=mu_hat, scale=np.sqrt(unbiased_sigma_squared), size=n)
    sample_variance = np.var(sample, ddof=1)  # Unbiased variance
    chi_squared_values.append((n - 1) * sample_variance / unbiased_sigma_squared)

# Plot the distribution of Chi-Squared statistic
plt.hist(chi_squared_values, bins=30, density=True, alpha=0.6, label="Simulated Chi-Squared")
plt.title("Distribution of $(n-1)\hat{\sigma}^2 / \sigma^2$")
plt.xlabel("Value")
plt.ylabel("Density")
plt.legend()
plt.show()

# Results
print(f"mu_hat : {mu_hat}")
print(f"sigma_squared_hat: {sigma_squared_hat}/")
print(f"unbiased_sigma_squared: {unbiased_sigma_squared}")
