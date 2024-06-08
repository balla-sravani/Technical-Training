s=input()
stack=[]
f=0
c=0
for i in s:
    if i=='(' or i=='{' or i=='[':
        stack.append(i)
    elif(not stack):
        if(i==')' and stack[-1]=='(' or i=='}' and stack[-1]=='{' or i==']' and stack[-1]=='['):
            stack.pop()
        else:
            print(c)
            f=1
            break
    else:
        print(c)
        f=1
        break
    c=c+1
if f==0:
    print("-1")
    
        
        