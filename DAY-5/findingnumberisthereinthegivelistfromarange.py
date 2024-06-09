""" here n=7 we should take range from 1 to 7 and compare that range with given list while compare if we found any missg number return thar number"""

n=int(input())
l=[0,5,3,6,7,2,1]
'''
for i in range(n+1):
    if i in l:
        continue
    else:
        k=i
print(k)'''
n=7
b=sum(l)
print(b)
n=(n*(n+1))//2
print(n)
print(n-b)

    

    
        
