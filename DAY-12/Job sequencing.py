'''
#job sequencing
#input:
#l1=[(1,3),(2,5),(4 ,6),(6,7),(5,8),(7,9)]
#a=[5,6,5,4,11,2]
#output:
#[5, 6, 10, 14, 17, 16]
#Max profit::17'''

l1=[(1,3),(2,5),(4 ,6),(6,7),(5,8),(7,9)]
a=[5,6,5,4,11,2]
b=a.copy()
i=1
while(i<len(l1)):
    j=0
    while(j<i):
        if l1[j][1]<=l1[i][0]:
            if b[j]+a[i]>b[i]:
                b[i]=b[j]+a[i]
        j+=1
    i+=1
print(b)
print(max(b))

