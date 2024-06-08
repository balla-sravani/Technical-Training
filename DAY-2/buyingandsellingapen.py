"'15 3 2 7 8 4: 6 buying a pen on the low cost day and selling in high cost day can buy on frist day can't sell and aat last day we can sell but can't buy"
l=list(map(int,input().split(",")))
p=0
buy=l[0]
for i in l:
    if i<buy:
        buy=i
    elif (i-buy)>p:
        p=i-buy
print(p)
'''
pr=0
for i in range(len(a)-1):
for j in range(i+1,len(a)):
if((a[i]<a[j] and a[j]-a[i]>pr):
pr=a[j]-a[i]
print(pr)
