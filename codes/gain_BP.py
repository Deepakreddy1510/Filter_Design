import numpy as np

# Given parameters
s1 = -0.1430 + 0.9863j
s2 = -0.3452 + 0.4085j
s3 = -0.3452 - 0.4085j
s4 = -0.1430 - 0.9863j 
epsilon = 0.49
Omega_Lp = 1

# Define denominator polynomial
den = np.poly([s1, s2, s3, s4])

# Define frequency range
w = np.arange(-2, 2.01, 0.01)

num = 0.2551

# Define parameters for transformation
B = 0.1188
Omega0 = 0.7138

# Perform transformation to get s_L
s_L = (1j * 0.6569)**2 + Omega0**2
s_L /= B * (1j * 0.6569)

H = num / np.polyval(den, s_L)
print(1 / abs(H))
