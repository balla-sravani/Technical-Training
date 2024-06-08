def fun(i,s1,s2):
    if(i==len(a)):
        return s1,s2
    if(a[i]%2==0):
        s1=s1+a[i]
    if(b[i]%2!=0):
        s2=s2+b[i]
    return fun(i+1,s1,s2)
            
a=[1,2,3,4]
b=[5,6,7,8]
x,y=fun(0,0,0)
print(x,y)