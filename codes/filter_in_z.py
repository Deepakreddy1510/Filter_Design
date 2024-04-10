import sympy as sp

# Define symbols
s, z = sp.symbols('s z')

# Given transfer function
Ha_BP_s = 8.7661e-5 * s**4 / (s**8 + 0.1473*s**7 + 2.7921*s**6 + 0.3075*s**5 + 2.9035*s**4 + 0.2124*s**3 + 1.3327*s**2 + 0.0485*s + 0.2278)

# Perform substitution
substitution = ((1 - z**-1) / (1 + z**-1))
substituted_expression = Ha_BP_s.subs(s, substitution)

# Simplify the expression
simplified_expression = sp.simplify(substituted_expression)

# Print the result
print("Expression in z:")
print(simplified_expression)


