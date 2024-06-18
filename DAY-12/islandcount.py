#input:5
#0 1 0 0 1
#1 0 0 1 1
#0 0 0 0 0
#1 0 0 0 0
#1 0 0 0 1
#output:5----count no.of islands
def fun(l,i,j,n):
    if l[i][j]==0:
        return
    if l[i][j]==1:
        l[i][j]=0
    if i>0:
        fun(l,i-1,j,n)
    if j>0:
        fun(l,i,j-1,n)
    if i<n-1:
        fun(l,i+1,j,n)
    if j<n-1:
        fun(l,i,j+1,n)
    
n=int(input())
res=0
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            res+=1
            fun(l,i,j,n)       
print(res)
