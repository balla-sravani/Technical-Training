''' paralelly two linked list '''
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
        
    def display(self):
        t=self.head
        while(t!=None):
            print(t.data,end="->")
            t=t.next
            
    def sum1(self):
        t=head
        s=0
        while(t!=None):
            s+=t.data
            t=t.next
        print(s)
        
    def lastnode(self,x):
        t=self.head
        while(t.next!=None):
            t=t.next
        t.next=node(x)
        
    def addbeg(self,x):
        if self.head==None:
            t=node(x)
            self.head=t
        else:
            t=node(x)
            t.next=self.head
            self.head=t
    
    def addevn(self):
        t=self.head
        s=0
        while(t!=None):
            if(t.data%2==0):
                s+=t.data
            t=t.next
        print(s)
            
    
l=sll()
l2=sll()
l.head=node(10)
l.lastnode(20)
l.lastnode(30)
l.lastnode(43)
l2.head=node(100)
l2.lastnode(200)
l2.addbeg(50)
l2.addbeg(40)
l2.display()
print()
l.display()
print()
l.addevn()
#l.sum1()
