def queen(r):
    if r==n:#row==n matrix j--row and i--col here
        return
    if r!=u:#when in row rook is not there
        for c in range(n):
            if(check(r,c)):#checking to place queen or not
                m[r][c]=1#palcing quuen at particular row or col
                break
            m[r][c]=0
        return queen(r+1)#checking next row
    else:
        queen(r+1)
       
def check(i,j):#passing row and col
    #if i==u:  #rook present in row or not
        #return 0
    if j==v:#rook present in col or not
        return
    r=i
    c=j
    for i in range(r+1):#row and col checking
        if m[i][j]==1:
            return 0
    i=r
    while(i>=0 and j>=0):#left diagional
        if m[i][j]==1:
            return 0
        i=i-1
        j=j-1
    while(r>=0 and c<n):#right diagonal
        if m[r][c]==1:
            return 0
        r=r-1
        c=c+1
    return 1
        
        
        
        
        
        
        
n=5
u=1
v=3
m=[]
for i in range(n):
    m.append([0]*n)
m[0][0]=1
queen(0)
print(m)
c=0
for i in range(len(m)):
    for j in range(len(m)):
        if m[i][j]==1:
            c+=1
print("the possible quuen are:")
print(c)