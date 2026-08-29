str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

d1 = {}
d2 = {}

for i in str1:
    if i in d1:
        d1[i] = d1[i] + 1
    else:
        d1[i] = 1

for i in str2:
    if i in d2:
        d2[i] = d2[i] + 1
    else:
        d2[i] = 1

if d1 == d2:
    print("Strings are Anagram")
else:
    print("Strings are not Anagram")