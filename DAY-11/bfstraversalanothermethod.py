def BFS(d,x):
    visited=[]  
    q=[x]      #append the start node to the queue
    while(q):
        for i in d[q[0]]:
            if i not in visited and i not in q:  
                q.append(i)
        a=q.pop(0)
        visited.append(a)
    return visited
d={1:[2,5],2:[1,3,5,4,6],3:[2,4],4:[2,3],5:[1,2],6:[2]}
print(BFS(d,1))