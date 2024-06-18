#Max area of the island
#input:
#5
#0 1 0 0 1
#1 0 0 1 1
#0 0 0 0 0
#1 0 0 0 0 
#1 0 0 0 1
#output:3
def area(l,n):
    m = 0
    def fun(i,j):
        if i < 0 or i >= n or j < 0 or j >= n or l[i][j] == 0:
            return 0
        if l[i][j] == 1:
            l[i][j] = 0
        area = 1
        area +=fun(i+1,j)
        area +=fun(i-1,j)
        area +=fun(i,j+1)
        area += fun(i,j-1)
        return area
    for i in range(n):
        for j in range(n):
            if l[i][j] == 1:
                c = fun(i,j)
                m = max(m,c)
    return m
    
n = int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split( ))))
print(area(l,n))
