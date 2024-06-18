def bfs(d,start):
    v=[start]
    q=[start]
    while len(q)!=0:
        a=q.pop(0)
        print(a,end=" ")
        for i in d[a]:
            if i not in v:
                v.append(i)
                q.append(i)
                
            
        
   
            






d={1:[2,3],2:[1,3,4],3:[1,2],4:[2]}
bfs(d,1)
