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

##Further computations
##below calculates the mutual information for I (X, Y) for a given count matrix nxy using values in problem / example
import numpy as np

def Ih(nxy):
    """
    Calculate Mutual Information (MI) I(X, Y) from a contingency table.
    
    Parameters:
    nxy : 2D numpy array (nx x ny table of counts)
    
    Returns:
    I : Mutual Information (MI) I(X, Y)
    """
    # Total sum of the contingency table
    n = np.sum(nxy)
    
    # Normalized table of proportions
    f = nxy / n
    
    # Row sums (marginal distribution for X)
    fx = np.sum(f, axis=1)
    
    # Column sums (marginal distribution for Y)
    fy = np.sum(f, axis=0)
    
    # Replace zeros in fx and fy with a small value (0.01)
    fx[fx == 0] = 0.01
    fy[fy == 0] = 0.01
    
    # Replace zeros in the normalized table f with a small value (0.01)
    f[f == 0] = 0.01
    
    # Calculate the outer product of fx and fy
    fxfy = np.outer(fx, fy)
    
    # Calculate the Mutual Information I(X, Y)
    I = np.sum(f * np.log(f / fxfy))
    
    return I

# Example usage:
##nxy = np.array([[30, 10], [10, 50]])  # Example contingency table but plug in problem values
nxy = np.array([
    [10, 9, 2],
    [10, 7, 2],
    [17, 11, 5],
    [22, 18, 7]
])

print(nxy)

mi_value = Ih(nxy)
print(f"Mutual Information: {mi_value}")


###not totally sure of this part
###experiement or simulations 
def sim(M, fxh, fyh):
    """
    Simulate Mutual Information (MI) values for M simulations.
    
    Parameters:
    M : int, number of simulations
    fxh : list or array, marginal distribution of X
    fyh : list or array, marginal distribution of Y
    

    Ihm : numpy array of simulated MI values (length M)
    """
    n = np.sum(nxy)##n = 120  # Number of samples to match the table
    print(n)
    nx = len(fxh)  # Number of unique X values
    ny = len(fyh)  # Number of unique Y values
    
    Ihm = np.zeros(M)  # Initialize vector to store MI results
    
    for m in range(M):
        # Sample from the marginal distributions
        xm = np.random.choice(np.arange(1, nx + 1), n, p=fxh, replace=True)
        ym = np.random.choice(np.arange(1, ny + 1), n, p=fyh, replace=True)
        
        # Create a contingency table from the sampled values
        nxym = np.zeros((nx, ny))
        for i in range(n):
            nxym[xm[i] - 1, ym[i] - 1] += 1
        
        # Calculate Mutual Information for the current simulation
        Ihm[m] = Ih(nxym)
    
    return Ihm

# Example usage:
# Define marginal distributions for X and Y
fxh = [0.25, 0.25, 0.25, 0.25]  # Uniform marginal distribution for X --unsure if this is properly set up
fyh = [0.33, 0.33, 0.34]  # Nearly uniform marginal distribution for Y--unsure if this is properly set up

# Number of simulations
M = 100

# Running the simulations
Ihm_result = sim(M, fxh, fyh)


# Output the first few simulated MI values
print(Ihm_result[:10]) ##number of simulations can be adjusted in results


##last computation

def Ihmstar(Ihm):
    """
    Select threshold Ih* based on the 95th percentile from a list of Mutual Information (MI) values.
    
    Parameters:
    Ihm : list or numpy array of MI values from simulations
    
    Returns:
    Is : Threshold MI value (95th percentile)
    """
    M = len(Ihm)  # Get the number of MI values
    istar = round(0.95 * M)  # 95th percentile index
    Is = np.sort(Ihm)[istar]  # Sort the MI values and select the 95th percentile
    
    return Is

print(Ihm_result)


# Example usage:
# Simulated Mutual Information values (Ihm) from 10 simulations
Ihm_values = np.random.rand(100)  # Example random MI values (0 to 1)

# Calculate the 95th percentile threshold
threshold = Ihmstar(Ihm_values) ##not sure if should be random  or the Ihm_result derived think threshold2 is right....
threshold2 = Ihmstar(Ihm_result)

# Output the threshold value
print(f"The 95th percentile MI threshold 1 is: {threshold}")
print(f"The 95th percentile MI threshold 2 is: {threshold2}")##believe threshold2 is correct / to be utilized further

