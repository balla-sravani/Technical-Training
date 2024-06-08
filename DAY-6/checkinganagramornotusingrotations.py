''' ip:
  school as a string
  query as integer:3(how many rotations will be performed)
  l2=left rotate 2-->hoolsc
  r3=rightrotate 3-->oolsch
  l1=left rotate 1-->chools
  take frist character in all the rotations
  hoc
  the substrings in the string are:
  sch,cho,hoo,ool
  then check hoc is anagram of school
   op: yes since coh is has similar words of hoc'''
'''input:school
       3
output:-
[['s', 'c', 'h'], ['c', 'h', 'o'], ['h', 'o', 'o'], ['o', 'o', 'l']]
yes ['c', 'h', 'o']'''

s=input()
n=int(input())
l1=[2,3,1]
l=[]
s=list(s)
for i in range(len(s)):
    for j in range(i+1,len(s)):
        sub=s[i:j+1]
        if len(sub)==n:
            l=l+[sub]
            #print(sub)
print(l)
s1=[]
for i in l1:
    s1=s1+list(s[i])
#s1=s1.sort()
s1.sort()
if s1 in l:
    print("yes",s1)
'''input:school
       3
output:-
[['s', 'c', 'h'], ['c', 'h', 'o'], ['h', 'o', 'o'], ['o', 'o', 'l']]
yes ['c', 'h', 'o']'''