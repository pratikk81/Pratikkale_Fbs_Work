#write a program to calculatt factorial using recusive function
def sOS(n):
    if(n>0):
        #print(n)
        return n * sOS(n-1)
    else:
        return 1
n=5 
res = sOS(n)   
print(res)