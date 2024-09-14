#KL Divergence & MI (Mutual Information) Simulation
import numpy as np

# Given count data (generate this from table in the problem/example to work with...)
counts = np.array([[12, 11, 7],
                   [11, 15, 6],
                   [10, 12, 9],
                   [7, 9, 10]])
print(counts)

# Total count
n_total = np.sum(counts)
print(n_total)

# Joint probability distribution f_{X,Y}(x,y)
f_XY = counts / n_total
print(f_XY) 


# Compute marginal probabilities
f_X = np.sum(f_XY, axis=1)  # Sum over rows
f_Y = np.sum(f_XY, axis=0)  # Sum over columns
print(f_X) #Compare to problem / example given
print(f_Y) #Compare to problem / example given

# Estimate mutual information or MI given formula
mi = 0
for i in range(f_XY.shape[0]):
    for j in range(f_XY.shape[1]):
        if f_XY[i, j] > 0:  # Avoid log(0)
            mi += f_XY[i, j] * np.log(f_XY[i, j] / (f_X[i] * f_Y[j]))

mi = mi / np.log(2)  # Convert to bits (log base 2)---check later
print("Estimated Mutual Information (I):", mi)


##Simulation Part & Decision Logic (Based on Problem Logic)
# Simulate under independence assumption
n_simulations = 1000
simulated_mi = []

for _ in range(n_simulations):
    # Generate a table under independence
    simulated_counts = np.random.multinomial(n_total, np.outer(f_X, f_Y).ravel()).reshape(f_XY.shape)
    
    # Compute joint probabilities
    simulated_f_XY = simulated_counts / n_total
    
    # Compute mutual information for the simulation
    sim_mi = 0 ##must always also = 0?
    for i in range(simulated_f_XY.shape[0]):
        for j in range(simulated_f_XY.shape[1]):
            if simulated_f_XY[i, j] > 0:  # Avoid log(0)  but explain....
                sim_mi += simulated_f_XY[i, j] * np.log(simulated_f_XY[i, j] / (f_X[i] * f_Y[j]))

    sim_mi = sim_mi / np.log(2)  # Convert to bits (log base 2) but explain rationale
    simulated_mi.append(sim_mi)

# Compare observed MI with simulated MI
p_value = np.mean(np.array(simulated_mi) >= mi) ##rationale
mid_point = np.mean(np.array(simulated_mi))

#value "midpoint" checks
print (mid_point)
print(sim_mi)
print(mi)
print(p_value)

#final p-value
print("P-value:", p_value)

#interpreting p-value / results
if p_value < 0.05:
    print("Reject null hypothesis, X and Y are dependent.")
else:
    print("Fail to reject null hypothesis, X and Y are independent.")

