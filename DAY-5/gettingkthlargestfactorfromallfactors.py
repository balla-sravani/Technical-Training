n=int(input())
k=int(input())
c=0
for i in range(1,n):
    if(n%i==0):
        r=(n//i)
        c+=1
    if(k==c):
        print(r)
        break
    
    