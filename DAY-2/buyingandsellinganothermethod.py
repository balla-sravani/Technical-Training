a=[15,3,2,8,1,4,9]
pr=0
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        if((a[i]<a[j] and a[j]-a[i]>pr)):
            pr=a[j]-a[i]
print(pr)