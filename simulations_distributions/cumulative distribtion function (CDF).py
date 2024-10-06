#CFD for random variable problem / example --refer to problem 3 in exam 1 prob practice 

import numpy as np
import matplotlib.pyplot as plt

# Given data
y_values = np.array([0, 2, 4])
p_y = np.array([0.1, 0.3, 0.6])

# 3a. Cumulative Distribution Function (CDF)
F_y = np.cumsum(p_y)  # CDF is cumulative sum of probabilities

# Extending the CDF for y < 0 and y >= 4
y_ext = np.array([-2, 0, 2, 4, 6])
F_y_ext = np.array([0, 0.1, 0.4, 1, 1])

# 3b. Plot the CDF
plt.step(y_ext, F_y_ext, where='post', label='CDF', color='blue')
plt.xlabel('y')
plt.ylabel('F(y)')
plt.title('Cumulative Distribution Function of Y')
plt.xlim(-2, 6)
plt.ylim(0, 1.2)
plt.grid(True)
plt.show()

# 3c. Expected Value and Variance
E_Y = np.sum(y_values * p_y)  # E(Y) = sum of y * p(y)
E_Y_squared = np.sum((y_values ** 2) * p_y)  # E(Y^2) = sum of y^2 * p(y)
Var_Y = E_Y_squared - E_Y ** 2  # Var(Y) = E(Y^2) - [E(Y)]^2

# Print results
print(f"E(Y): {E_Y}")
print(f"Var(Y): {Var_Y}")
