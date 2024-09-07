# Simulation problem HW 1
import numpy as np
import matplotlib.pyplot as plt 

def simulate_pr_b_given_a(p=0.02, n=10000):
    # Declare sensitivity and specificity 
    sens = 0.999
    spec = 1 - 0.005
    
    # Generate B (whether subjects have genetic disorder)
    B = np.random.choice([0, 1], size=n, p=[1-p, p])
    
    # Simulate test results
    u = np.random.uniform(size=n)
    A = np.where((B == 1) & (u < sens), 1, np.where((B == 0) & (u > spec), 1, 0))
    
    # Calculate empirical frequencies
    nBA = np.sum(A & B)  # Num of subjects positive for test & disorder
    nA = np.sum(A)       # Num of positive test results 
    
    # Probability of having the disorder given positive test result
    if nA > 0:
        return nBA / nA
    else:
        return 0

# Create grid & calculate probabilities
p_grid = np.linspace(0.01, 0.5, 100)
y = [simulate_pr_b_given_a(p) for p in p_grid]

# Plot the result
plt.plot(p_grid, y, '-o')  # Corrected marker style
plt.xlabel("Pr(B) (probability of having disorder)")
plt.ylabel("Pr(B|A) (probability of disorder given positive test)")
plt.title("Probability of Disorder Given Positive Test Result")
plt.grid(True)
plt.show()
