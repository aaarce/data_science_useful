import numpy as np

# Given data
n_agree = 38
n_total = 130
n_resamples = 10000  # Number of bootstrap resamples can adjust but recommended is minimum 5000
confidence_level = 0.92

# Step 1: Set up the data (1 for agree, 0 for disagree)
data = np.array([1] * n_agree + [0] * (n_total - n_agree))

# Step 2: Bootstrap resampling with replacement
bootstrap_samples = np.random.choice(data, size=(n_resamples, n_total), replace=True)
bootstrap_proportions = np.mean(bootstrap_samples, axis=1)

# Step 3: Calculate the confidence interval with standard formula 
lower_percentile = (1 - confidence_level) / 2 * 100
upper_percentile = (1 + confidence_level) / 2 * 100


confidence_interval = np.percentile(bootstrap_proportions, [lower_percentile, upper_percentile])
confidence_interval_l = np.percentile(bootstrap_proportions, lower_percentile)
confidence_interval_u = np.percentile(bootstrap_proportions,  upper_percentile)



print(f"{confidence_level*100}% confidence interval for the population proportion is {confidence_interval}")

# Step 4: Calculate length of the interval
print(f"{confidence_interval_u-confidence_interval_l} is the confidence interval length")

