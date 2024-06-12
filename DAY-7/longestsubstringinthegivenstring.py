'''
length of a longest substring
ip:"abfgresagtyuiofde"
in the above string from r to d no repeation 
op:12
d={}
d={a:0,b:1,f:2,g:3,r:4,e:5,s:6,}
s="abfgres"
m=0
then m=7
then s=" " --->empty
next i=i+1 --->a=0+1=1 it start from b
stop when i>len(string)
''' 
a='abfgresagtyauiofde'
d={}
s=""
m=0
n=len(a)
i=0
while i<n:
    if a[i] not in s:
        s+=a[i]
        d[a[i]]=i
    else:
        if len(s) > m:
            m=len(s)
        s=""
        i=d[a[i]]
    i+=1
print(m)
       
        
        


