'''ip:
l=[4,8,14,22,37,68]
all the elements in array are non primes in incresing order
then take a list and append the max prime number between the range of every 2 elements and find sum of all that prime numbers
op:
prime from 4,8---->7
prime from 8,14---->13
prime from 14,22---->19
prime from 22,37---->31
prime from 37,68---->67

7 13 19 31 67'''

def isprime(x):
    for i in range(2,(x//2)+1):
        if x%i==0:
            return 0
    return 1
        
        
def lprime(n,m):
    for i in range(m-1,n,-1):
        if(isprime(i)):
            return i
    return 0
        
    
a=[4,8,14,22,37,68]
s=0
for i in range(len(a)-1):
    s=s+lprime(a[i],a[i+1])

print(s)
        
        

    
        
        
        
        
            

