'''finding the number in the array which has highest count in the array'''
''' next 8 again new decement count and w=8 and make c=1 for 2 and make w=2 and new person  c=2 and w=4 and if cuurent and w is same incement when c=0 then only update the w ''' 


'''a=[4,5,6,6,7,7,7,8]
max=0
for i in a:
    if (a.count(i)>max):
        max=a.count(i)
        p=i
print(p)'''
l=[1,1,2,2,1,3]
c=1
w=l[0] 
for i in range(len(l)):
    if l[i]==w:
        c+=1
    else:
        if c!=0:
            c-=1
        else:
            c=1 ''' count should not go to zero'''
            w=l[i]
print(w)
    
