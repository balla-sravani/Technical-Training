''''
5--2----8----4---6\
| \      |         2
|   \    |          \
|2    \2 | 3          9--2-4
|     \  |          /
|      \ |        /1                       l=[]
2---1---3---3---7 /
1.start at 5 .
look at 2 and 8 and 3 neigbours all are 2 but 5 to 9 we should find least path
to reach 5 cost is 0 to go to 8 cost is 2. then from 8 to 6
v=[]
q=[5,2,3,8]
pop 5
v=[(5,0),(2,2)]#0 is the cost
q=[3,8,]
6:pop 2
'''
'''def fun(g,x):
    d={5:9999,1:9999,3:9999,6:9999,2:9999}
    d[x]=0
    vi=[]
    q=[x]
    while(q):
        m=9999
        for i in q:
            if d[i]<m:
                m=d[i]
                x=i
       
        for i in g[x]:
            if(i[0] not in vi):
                q.append(i[0])
                if d[i[0]]>i[1]+d[x]:
                    d[i[0]]=i[1]+d[x]  
        vi.append(x)
        q.remove(x)
    print(d)

    
g={5:[(3,1),(1,2),(6,3)],1:[(5,2),(2,1)],3:[(5,1),(6,3)],6:[]}
print(fun(g,5))'''
def bfs(s):
    d={5:9999,7:9999,4:9999,8:9999,3:9999,2:9999}
    d[s]=0
    v=[]
    q=[s]
    
    while q:
        m=9999
        for i in q:
            if(d[i]<m):
                m=d[i]
                s=i
        
        for i in graph[s]:
            if i[0] not in v: 
                q.append(i[0])
                if d[i[0]]>i[1]+d[s]:
                    d[i[0]]=i[1]+d[s]
            
        v.append(s)
        q.remove(s)
    print(d)
    #print(v)
graph={5:[(7,2),(3,4)],
       7:[(5,2),(4,1),(3,2)],
       4:[(7,1),(8,1),(2,3)],
       8:[(3,3),(4,1),(2,5)],
       3:[(5,4),(7,2),(8,3)],
       2:[(4,3),(8,5)]}
bfs(5)