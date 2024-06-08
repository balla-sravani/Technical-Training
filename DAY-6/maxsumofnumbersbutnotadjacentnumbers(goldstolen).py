'''ip:[13,9,4,10,5,7]
op:30 since max gold to be stolen from the houses but no adjacent houses'''
def fun(l):
    if len(l)==0:
        return 0
    if len(l)==1:
        return l[0]
    if len(l)==2:
        return max(l)
    le=l[0]+fun(l[2:])
    ri=l[1]+fun(l[3:])
    return max(le,ri)

l=[9,1,19,20,30,3]
res=fun(l)
print(res)
    