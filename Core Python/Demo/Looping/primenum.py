#num = int(input('enter the number'))
start = int(input('enter starting number'))
end = int(input('enter the number'))
print(f'the prime no form{start}to{end}')
for num in range(start,end):

    if num>1:
        for i in range(2,num):
         if num%i==0:
            break
  

    else:
        print(num)
else:
    print('the number is not prime or composite')        