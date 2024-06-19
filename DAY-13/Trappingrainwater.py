'''
Trapping rain water

l=[2,5,2,3,6,7,1,0,5,7]
2 5 5 5 6 7 7 7 7 7 ---->front to back
7 7 7 7 7 7 7 7 7 7----->back to front
take minimum from those 2 arrays and subtract respective building height then store that value is nothing but water stored

suppose 2 building then 5 >2 update again 2>5 no be same 5 if after number greater than before one then only update
other wise no'''
'''l=[2,5,2,3,6,7,1,0,5,7]
a=[l[0]]
b=[l[-1]]
i=1
for i in range(len(l)-1):
    if l[i]>l[i+1]:
        a.append(l[i])
    else:
        a.append(l[i+1])
print(a)
   
#l=[2,5,2,3,6,7,1,0,5,7]
l=[4,3,4,5,6,1,0,6,7]
max1=l[0]
max2=l[-1]
c=0
for i in range(len(l)):
    if l[i]>max1:
        max1=l[i]
    for j in range(0,len(l),-1):
        if l[j]>max2:
            max2=l[j]
    k=min(max1,max2)
    c+=k-l[i]
print(c)'''
arr=[4,3,4,5,6,1,0,6,7]
l=[0]*len(arr)
r=[0]*len(arr)
m=0
m1=0
for i in  range(len(arr)):
    if arr[i]>m:
        m=arr[i]
    l[i]=m
for i in range(len(arr)-1,-1,-1):
    if arr[i]>m1:
        m1=arr[i]
    r[i]=m1
s=0
for i in range(len(arr)):
    s=s+abs(min(l[i],r[i])-arr[i])
print(s)
    
    
            
    
    
    

