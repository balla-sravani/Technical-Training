'''ip:
 "hello:5438,car:214,book:8799,apple:2187"
 frist take length of key and comapre with values
 hello---->5 and 5 is present in value so give 5th character 0 if it is not present then take decrement value of that number
 op: oxap'''

d={
    "hello":5438,
    "car":214,
    "book":8799,
    "apple":2187}

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
            
  

    