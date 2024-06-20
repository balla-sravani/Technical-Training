arr=[3,5,9,6,8,10]
m=0
c=0
c1=0
m1=0
l=[0]*len(arr)
r=[0]*len(arr)
for i in  range(len(arr)):
    if arr[i]>m:
        m=arr[i]
        c+=1
    l[i]=m
for i in range(len(arr)-1,-1,-1):
    if arr[i]>m1:
        m1=arr[i]
        c1+=1
    r[i]=m1
print(" letf side houses:",c)
print("right side houses:",c1)
