#ANOVA Test for Difference in Means Using F-Statistic Example Problem ---Note, dataset is Locke & below gives same computations for problem as Statkey
#" In the TextbookCosts dataset, the variable Cost is the “Total Cost (in dollars) per course for 
#the required books.” Test the claim that there is a difference in the average of the Cost variable in the 
#several “fields” of study. Do this using a theoretical dist’n. "

###other
import numpy as np
import scipy.stats as stats

# Given data in dataset mentioned --- note entering this into StatKey or in table makes this easier
sample_sizes = [10, 10, 10, 10]  # Sample sizes for the four groups
means = [118.3, 170.8, 120.3, 94.6]  # Means of the four groups
std_devs = [48.9, 48.5, 58.1, 44.9]  # Standard deviations of the four groups

# Calculate the variance for each group (standard deviation squared)
variances = [std**2 for std in std_devs]

# Use the formula for between-group variance and within-group variance
# Between-group variance formula given
SSB = sum(sample_sizes[i] * (means[i] - np.mean(means))**2 for i in range(len(sample_sizes)))

# Within-group variance formula given 
SSW = sum((sample_sizes[i] - 1) * variances[i] for i in range(len(sample_sizes)))

# Degrees of freedom calculation 
dfb = len(means) - 1  # Between group degrees of freedom
dfw = sum(sample_sizes) - len(means)  # Within group degrees of freedom

# Mean square between and within groups
MSB = SSB / dfb
MSW = SSW / dfw

# F-statistic
F = MSB / MSW

# Calculate the p-value from the F-distribution
p_value = 1 - stats.f.cdf(F, dfb, dfw)


print(f"F-statistic: {F}")
print(f"P-value: {p_value}")
