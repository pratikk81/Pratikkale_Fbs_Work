def armstrong(num):
    
    count = len(str(num))
    sum = 0

    while num > 0:
        digit = num % 10
        sum = sum + digit**count
        num = num // 10
        return sum
num = int(input("Enter a number: "))  
result= armstrong(num) 

if result == num:
    print(num, "is an Armstrong Number.")
else:
    print(num, "is not an Armstrong Number.")



armstrong(num)