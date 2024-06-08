class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def display(self):
        t=head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
    def lastnode(self,x):
        t=head
        while(t.next!=None):
            t=t.next
        t.next=node(x)
    def sliding(self):
        temp=head
        c=1
        m=0
        while(temp.next.next!=None):
            if temp.data==temp.next.data-1:
                c=c+1
                temp=temp.next
                if c>m:
                    m=c   
            else:
                temp=temp.next
        print(m)
    def allpairs(self):
        t=head
        while(t.next!=None):
            t1=t.next
            while(t1!=None):
                print(t.data,t1.data)
                t1=t1.next
            t=t.next
    def bubblesort(self):
        t=head
        t1=head.next
        while(t!=None and t1!=None):
            while(t1!=None):
               if (t.data>t1.data):
                    t.data,t1.data=t1.data,t.data
                    t1=t1.next
               else:
                    t1=t1.next
            t=t.next
            t1=t.next
    def bubble(self):
        T=head
        c=0
        p=None
        while(T.next!=None):
            f=0
            t=head
            while(t.next!=p):
                if (t.data>t.next.data):
                    f=1
                    t.data,t.next.data=t.next.data,t.data
                t=t.next
                c+=1
            if f==0:
                break
            p=t
        print(c)
            
                
            

        
    
            
        
        
   
            
            
    
l=sll()
head=node(1)
l.lastnode(2)
l.lastnode(3)
l.lastnode(8)
l.lastnode(7)
l.lastnode(8)
l.lastnode(2)
l.lastnode(3)
l.lastnode(1)
l.lastnode(5)
l.display()
print()
l.sliding()
l.allpairs()
l.bubblesort()
l.display()
print()
l.bubble()
l.display()


