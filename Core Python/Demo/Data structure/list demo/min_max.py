li = [10,9,1,33,46]
max =li[0]
min =li[0]

for i in li:
    if i > max:
        max = i
    if i < min:
        min = i
print('list :',li)

print('maximum number of list is :',max)
print('minimum number of list is :',min)
            