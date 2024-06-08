'''take 3x3 matrix frist
xyz
pqr
abc
yraxpazr => yes'''

'''
n=int(input())
l=[]
for i in range(n):
    m=list(map(str,input().split()))
    l.append(m)
print(l)
s=input()
f=0
for i in range(len(s)):
        if( s[i] in l[i]):
            continue
        else:
            f=1
            break
if(f==1):
    print("yes")
else:
    print("no")
'''

n=int(input())
m=[]
for i in range(n):
    m.append(input())
print(m)
s=input()
for i in range(len(s)):
        if (s[i] not in m[i%n]):
            print("no")
            break
else:
    print("yes")