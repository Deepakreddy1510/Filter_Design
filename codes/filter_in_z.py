import sympy as sp

# Define symbols
s, z = sp.symbols('s z')

# Given transfer function
Ha_BP_s = 5.6489e-5 * s**4 / (s**8 + 0.1160*s**7 + 2.0588*s**6 + 0.1786*s**5 + 1.5790*s**4 + 0.0909*s**3 + 0.5345*s**2 + 0.0153*s + 0.0674)

# Perform substitution
substitution = ((1 - z**-1) / (1 + z**-1))
substituted_expression = Ha_BP_s.subs(s, substitution)

# Simplify the expression
simplified_expression = sp.simplify(substituted_expression)

# Print the result
print("Expression in z:")
print(simplified_expression)


