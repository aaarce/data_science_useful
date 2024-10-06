#statistical practice exam 1 single-proportion example
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



print(f"{confidence_level*100}% confidence interval for the population proportion is {confidence_interval}") #note very close to statkey interval obtained with random bootstrap simulations

# Step 4: Calculate length of the interval
print(f"{confidence_interval_u-confidence_interval_l} is the confidence interval length") #answers are to be calculated & submitted in this format but interval is much more interesting

#difference in two proportions example hypothesis test note statkey used for answers but double-check w/ python
import numpy as np
from scipy import stats

# Given data
n_men = 242
x_men = 74  # Men who agree
n_women = 282
x_women = 72  # Women who agree

# Step 1: Calculate sample proportions
p_men = x_men / n_men
p_women = x_women / n_women

# Step 2: Calculate pooled proportion
p_pooled = (x_men + x_women) / (n_men + n_women)

# Step 3: Compute the standard error
se = np.sqrt(p_pooled * (1 - p_pooled) * (1/n_men + 1/n_women))

# Step 4: Calculate the z-score
z = (p_men - p_women) / se

# Step 5: Compute the p-value (one-sided test)
p_value = 1 - stats.norm.cdf(z) #note this fairly close / comparable to statkey p-value

# results
print(f"Z-value: {z}")
print(f"P-value: {p_value}")
