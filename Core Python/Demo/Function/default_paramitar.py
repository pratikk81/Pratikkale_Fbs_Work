#1. To make parameter optional
#2. Assign value to parameter in function definition
#3. If we pass value to defult parameter it takes  passsed value 
#   If we don't pass value to defult parameter it takes defult value 
#4. Flow form right to left

def emp(id,name,sal=10000,dept='IT'):
    print('id :',id)
    print('name :',name)
    print('salary :',sal)
    print('department :',dept)

emp(101,'om',50000,'DA')
print('################################')
emp(102,'pratik',70000)
print('################################')
emp(103,'mahesh')

