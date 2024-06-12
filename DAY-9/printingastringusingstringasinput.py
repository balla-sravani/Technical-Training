d={}
a=input().split(',')
for i in range(len(a)):
    b=a[i].split(":")
    print(b[0],b[1])
    d[b[0]]=b[1]
print(d)
res=""
flag=1
for i in d:
    c=len(i)
    while flag:
        if (str(c) in str(d[i])):
            c=int(c)
            res+=i[c-1]
            flag=0
        elif c<0:
            res+='x'
            flag=0
        elif str(c) not in str(d[i]):
            c=int(c)
            c=c-1
    flag=1
print(res)
            
  
