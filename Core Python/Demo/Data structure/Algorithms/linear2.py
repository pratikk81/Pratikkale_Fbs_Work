li=[12,32,45,18,67,90]
target =int(input('enter a number you want to a search :'))
for el in li:
    if el==target:
        print(f'{target} is found')
        break
    else:
        print(f'{target} is not found')