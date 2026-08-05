#reduce line of code

#data=[1,2,3,4,5,6,7,8,9,10]
#res = list(map(lambda num: num*num,data))
#print(res)

li=[12,3.11,4,5]
#res=map(lambda x:x**2,li)
res=filter(lambda x:x%2==0,li)
#print(type(res))
print(list(res))