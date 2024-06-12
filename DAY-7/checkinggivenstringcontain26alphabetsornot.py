'''
ip:the quick brown fox jumps over the lazy dog
op: yes since it contain 26 alphabets
ip:qwweer yuiop asdfvgh jkl mnbvlkjcxz"
op:no'''
s="qwweer yuiop asdfvgh jkl mnbvlkjcxz"
s1="abcdefghijklmnopqrstuvwxyz"
c=0
for i in s1:
    if i  not in s:
        print("no")
        break
else:
    print("yes")

s="qwweer yuiop asdfvgh jkl mnbvlkjcxz"
s1=97
for i in range(97,123):
    if chr(i) not in s:
        print("no")
        break
else:
    print("yes")
    
a="qwweer yuiop asdfvgh jkl mnbvlkjcxz"
d=set()
d.add(i)
for i in a:
    if(i.islower()):
        d.add(i)
print(d)

#hashmap
a="the quick brown fox jumps over the lazy dog"
d=[0]*26
for i in a:
    if(i.islower()):
        d[ord(i)-97]+=1
print(all(d))
    
    
