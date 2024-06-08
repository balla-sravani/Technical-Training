class node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
class dll:
    def __init__(self):
        self.head=None
        self.tail=None
    def insert_End(self,x):
        if self.head==None:
            self.head=node(x)
            self.tail=self.head
        else:
            newnode=node(x)
            self.tail.next=newnode
            newnode.prev=self.tail
            self.tail=self.tail.next
            
    def insert_Begin(self,x):
        if self.head==None:
            self.head=node(x)
            self.tail=self.head
        else:
            newnode=node(x)
            newnode.next=self.head
            self.head.prev=newnode
            self.head=newnode
    def traverse(self):
        temp=self.head
        while(temp!=None):
            print(temp.value,end="->")
            temp=temp.next
        print()
    def rev(self):
        temp=self.tail
        while(temp!=None):
            print(temp.value,end="->")
            temp=temp.prev
    def linearsearch(self,x):
        t=self.head
        s=self.tail
        f = 0
        while(t.next!=None and s.prev!=None):
            if(x == t.value or x == s.value):
                f=1
                break
            else:
                t=t.next
                s=s.prev
        
        if f==1:
            print("Yes")
        else:
            print("No")
    def length(self):
        t=self.head
        s=self.tail
        f=0
        while(t.next!=None and s.prev!=None):
            t = t.next
            s = s.prev
            if t==s:
                f=1
                break
        if f==1:
            print("odd")
        else:
            print("even")


l=dll()
l.insert_Begin(10)
l.insert_Begin(20)
l.insert_Begin(30)
l.insert_End(40)
l.insert_End(50)
l.traverse()
l.rev()
print() 
l.linearsearch(50)
l.length()
'''
f=h
s=h
while(f!=N):
f=f.n.n
s=s.n
s.t.n=s.h
s.h.p=s.t
t1=s.p
t1.n=N
s.h=s
s.t=t1'''
