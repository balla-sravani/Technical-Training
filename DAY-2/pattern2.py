'''ip:4
   ----a----
   ---aba---
   --abcba--
   -abcdcba-'''
#input:4
#output:
#    _ _ _ _ a_ _ _ _
#    _ _ _a  b  a _ _ _
#    _ a  b c b  a _
#    _a  b  c  d  c  b  a _
n=int(input())
j=1
for i in range(n,0,-1):
    print('_'*i,end=" ")
    a=97
    for k in range(j):
        print(chr(a),end=" ")
        a+=1
    a=97
    for k1 in range(j-1):
        print(chr(a),end=" ")
        a+=1
    print('_'*i,end=" ")
    j=j+1
    print()
    
        
         