""" 
ip: abc
    xya
    pqc
s:ayccax: yes
s:axpbbq: no since duplicate should not be there in the string"""

n=int(input())
m=[]
for i in range(n):
    m.append(list(input()))
print(m)
s=input()
f=0
for i in range(len(s)):
        if (s[i] not in m[i%n]):
            print("no")
            f=1
            break
        else:
            m[i].remove(s[i])
if(f==0):
    print("yes")
