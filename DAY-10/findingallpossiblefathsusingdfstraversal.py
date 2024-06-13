def dfs(start,l,d):
    l.append(start)
    if(start==2):
        print(l)
        return
    for i in d[start]:
        if i not in l:
            dfs(i,l,d)
            l.pop()
l=[]
d={5:[7,3],7:[5,4,3],4:[7,8,2],8:[3,4,2],3:[5,7,8],2:[4,8]}
src=int(input())
dfs(src,l,d)

