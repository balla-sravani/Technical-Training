s=input()
n=int(input())
l=[]
for i in range(len(s)-n+1):
    l.append(list(s[i:n+i]))
print(l)
    
    
    