def rev(n,r):
    if(n==0):
        return r
    r=r*10+(n%10)
    return rev(n//10,r)
        
n=int(input())
res=rev(n,0)
if res==n:
    print("is palindrome")
else:
    print("not palindrome")


    