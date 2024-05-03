import numpy as np
from scipy.optimize import minimize_scalar

def diode_equation(n, V, I):
    VT = 0.026
    return sum((I - np.exp(V / (n * VT)) + 1) ** 2)

V_data = np.array([0.7499, 0.7157, 0.6842, 0.6550, 0.0044])
I_data = np.array([0.35, 0.3, 0.24, 0.2, 0,1])

result = minimize_scalar(diode_equation, args=(V_data, I_data))
n_estimate = result.x

print(f"Estimated ideality factor (n): {n_estimate:.4f}")
