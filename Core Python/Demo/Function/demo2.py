def chkPallindrome():
    num = int(input('enter number:'))
    temp = num
    rev =0

    while(temp > 0):
        d = temp % 10
        temp = temp // 10
        rev = rev * 10 + d
        print(rev)

    if(num == rev):
        print('the number is pallindrom.')
    else:
        print('the number is not pallindrom')   

chkPallindrome()

