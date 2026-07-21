num = int(input('Enter value of n:'))

temp = num
rev = 0

while(num > 0):
    d = num % 10
    num = num // 10
    rev = rev * 10 + d
    #print(d)

if(temp == rev):
    print('number is pallindrom')
else:
    print('number is not oallindrom')    