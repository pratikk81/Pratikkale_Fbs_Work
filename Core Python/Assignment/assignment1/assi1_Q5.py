P = float(input('Enter principle amount :'))
R = float(input('Enter Rate of interest :'))
T = float(input('Enter time in year :'))

A = P * (1 + R / 100) ** T
CI = A - P

print("Amount =", round(A, 2))
print("Compound Interest =", round(CI, 2))