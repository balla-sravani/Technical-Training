'''ip:
    6
    6
    0 1 1 1 0 1
    0 1 0 1 0 0
    1 0 1 1 0 0
    0 0 0 1 1 1
    1 1 0 0 0 1
    1 1 1 0 1 0
    4 6
    4 th row 6 th col tree cathes fire  it spread up left down right no diagonal
    8 trees are left'''


def fun(i,j,a,n):
    if i<0 or j<0 or i>=n or j>=n or a[i][j]!=1 :
        return
    if a[i][j]==1 :
        a[i][j]=2
    fun(i,j-1,a,n)
    fun(i-1,j,a,n)
    fun(i+1,j,a,n)
    fun(i,j+1,a,n)
    
a=[]
n=int(input())
for i in range(n):
    a.append(list(map(int,input().split())))
i=int(input())
j=int(input())
fun(i-1,j-1,a,len(a))
print(a)
c=0
for i in range(n):
    for j in range(n):
        if a[i][j]==1:
            c+=1
print(c)
    









'''
def fun(l,i,j):
    if i<0 or j<0:
        return l
    if i>=n or j>=n:
        return l
    else:
        fun(l,i,j)
        if l[i][j]==1:
            l[i][j]=2


  
'''
'''if l[i][j]==0:
        return
    if l[i][j]==1:
        l[i][j]=0
    if i<n-1:
        fun(l,i+1,j,n)
    if i>0:
        fun(l,i-1,j,n)
    if j>0:
        fun(l,i,j-1,n)
    if j<n-1:
        fun(l,i,j+1,n)
def burn(l,i,j,n):
    l[i][j]=2
    if
    
        
for i in range(n):
    for j in range(n):
        if l[i][j]==1:
            count+=1
            fun(l,i,j,n)'''
'''print(count)'''
l=[]
n=int(input())
for i in range(n):
    l.append(list(map(int,input().split())))
i=int(input())
j=int(input())
r=fun(l,i,j)
print(r)





    