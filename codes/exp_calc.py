from sympy import symbols, expand

# Define the symbolic variable s
s = symbols('s')

# Define the given values of s5, s6, s7, s8
s5 = -0.1430 + 0.9863j
s6 = -0.3452 + 0.4085j
s7 = -0.3452 - 0.4085j
s8 = -0.1430 - 0.9863j

# Calculate the product (s-s5)(s-s6)(s-s7)(s-s8)
product = expand((s - s5) * (s - s6) * (s - s7) * (s - s8))
print(product)

