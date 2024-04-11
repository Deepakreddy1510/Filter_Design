import sympy as sp
s = sp.symbols('s')
x = sp.symbols('x')
o = 0.7138 
B = 0.1188

s5 = -0.1430 + 0.9863j
s6 = -0.3452 + 0.4085j
s7 = -0.3452 - 0.4085j
s8 = -0.1430 - 0.9863j
Dr = sp.expand((s-s5)*(s-s6)*(s-s7)*(s-s8))
print(f"{Dr}")
s = (x**2 + o**2)/(B*x)
print('\n')
Dr_2 = sp.expand((s-s5)*(s-s6)*(s-s7)*(s-s8))
print(f"{Dr_2/5020.35279554985}") #coefficient of x^8 in order to normalize it.
print('\n')
print((0.2551*1.1117)/(5020.35279554985))
