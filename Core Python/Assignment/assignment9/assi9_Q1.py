
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def sum_series(n):
    if n == 1:
        return factorial(1)
    return factorial(n) + sum_series(n - 1)


n = int(input("Enter the value of n: "))

result = sum_series(n)

print("Sum of series =", result)