'''ip
#input:121
#output: 121 print same number  if it is palindrome
#input:122
#output:131 print next nearest palindeome
#input:1234
#output:1331
#input:24
#output:33
#input:1112
#output:1221
#input:7654
#output:7667
#input:56472
#output:56565
'''
def rev(n):
    t=n
    r=0
    while(n>0):
        r=r*10+(n%10)
        n=n//10
    if r==t:
        return t
    else:
        return rev(t+1)
  
n=int(input())
res=rev(n)
print(res)
