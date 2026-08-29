#1 structure : Denoted by[]
li=[10,20,30,40]
print(type(li))

#2 type of data :hetrogeneous
li=[10,3.14,'abc']
print(li)

#3 sequence; ordered

#4 changable: mutable
print(id(li))
li[1] = 17.35
print(id(li))
print(li)

#5 duplication: allowed
li = [10,10,20,30,10,20]
print(li)