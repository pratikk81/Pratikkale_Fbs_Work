di = {'id':101, 'name':'abc', 'dect': 'It'}

di.clear()
di2 = di.copy()


print(di.get('Id', 'key not found'))

print(di.items())
print(di.keys())
#res=di.pop('name')
#print(res)
#di.popitem()
di.update({'age': 25, 'add':'pune'})
print(di.values)