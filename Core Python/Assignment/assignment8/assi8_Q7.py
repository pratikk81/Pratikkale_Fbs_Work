# Function to find sum of digits

def sumDigits(num):
    total = 0

    while num > 0:
        digit = num % 10
        total = total + digit
        num = num // 10

    return total

# Main Program
num = int(input("Enter a number: "))

result = sumDigits(num)

print("Sum of digits =", result)