def emp(id,name,sal,dept):
    data = 'id:'+ str(id)+'\n'
    data +='name:'+ str(name)+'\n'
    data +='salary:'+ str(sal)+'\n'
    data +='department:'+ str(dept)+'\n'
    return data
res = emp(name ='abcd',id= 101,dept='IT',sal=50000)
print(res)