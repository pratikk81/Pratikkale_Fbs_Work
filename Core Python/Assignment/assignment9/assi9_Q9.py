# Recursive function to calculate m power n
def power(m, n):
    if n == 0:
        return 1
    return m * power(m, n - 1)


m = int(input("Enter the base (m): "))
n = int(input("Enter the exponent (n): "))

result = power(m, n)

print(f'{m} Raised to the power of {n} = {result}')