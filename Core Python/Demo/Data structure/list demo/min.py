li=[45,34,81,77,53,343,26,82]

min = li[0]
for ind in range(0,len(li)):
    if(li[ind]>min):
        min = li[ind]
        
print('minimum of element',min)