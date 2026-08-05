def chkStrong():
    num = int(input('enter number:'))
    temp = num
    sum=0

    d = temp % 10

    fact = 1
    for i in range(1, d + 1):
            fact = fact * i

    sum = sum + fact
    temp = temp // 10
      

    if( num==sum):
        print('the number is Strong')
    else:
        print('the number is not Strong')   

chkStrong()



