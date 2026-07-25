n = int(input("Enter number of students: "))

total_percentage = 0

for i in range(1, n + 1):
    print("Enter marks of Student", i)

    total = 0

    for j in range(1, 6):
        marks = int(input("Enter marks of Subject "))
        total = total + marks

    percentage = total / 5
    print("Percentage of Student", i, "=", percentage)

    total_percentage = total_percentage + percentage

average = total_percentage / n

print("Average Percentage of all students =", average)