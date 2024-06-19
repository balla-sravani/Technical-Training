'''
[1,3,4,5]
take minimum coins to get output
#6-3=3 go to 3 and take the value add +1 to the value
we should add coins and we can also consider the coins in multiple to get minimum coins


        0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
        
1       0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 
                    6-3=3+1
3       0 1 2 1 2 3 2 3 4 3  4  5  4  5  6  5  6  7

4       0 1 2 1 1 2 2 2 2 3  3  3  3  4  4  4  4  5

5       0 1 2 1 1 1 2 2 2 2  2  3  3  3  3  3  4  4

 op:17'''
'''n=int(input())
l=[3,4,5]
dp=[[0]*(n+1)]*(len(l))
k=0
for i in range(len(l)):
    for j in range(n+1):
        if i==0:
            dp[i][j]=j
        if j<l[i]:
            dp[i][j]=dp[i-1][j]
        if j>l[i]:
            k=j-l[i]
        dp[i][j]=min(dp[i-1][j],dp[i][k]+1)
print(dp)
print(dp[len(l)-1][n-1])'''

def fun(l,n):                # 0 1  2  3   4  5  6  7
    l1=[-1]*(n+1)            #[0,-1,-1,-1,-1,-1,-1,-1]-->#[-1,-1,1,1,-1,-1,2,2]
    l1[0]=0
    for i in l:#i=3
        for j in range(1,n+1):#it should start from 1 since l[0]=0 already
            if(j>=i):
                if(l1[j-i]!=-1):
                    if(l1[j]!=-1):
                        l1[j] = min(l1[j],l1[j-i]+1)
                    else:
                        l1[j]=l1[j-i]+1
    return (l1[-1])
l=list(map(int,input().split( )))
n=int(input())
print(fun(l,n))