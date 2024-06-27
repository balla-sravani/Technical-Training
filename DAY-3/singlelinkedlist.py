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
    def sum1(self):
        t=head
        s=0
        while(t!=None):
            s+=t.data
            t=t.next
        print(s)
    def lastnode(self,x):
        t=head
        while(t.next!=None):
            t=t.next
        t.next=node(x)
    def search(self,x):
        f=0
        t=head
        while(t.next!=None):
            if (x==t.data):
                f=1
                break
            else:
              t=t.next
        if(f==1):
            print("the element is found")
        else:
            print("the element is not found")
    def middle(self):
        s=head
        f=head
        while f and f.next:
            s=s.next
            f=f.next.next
        print(s.data)
    def length(self):
        t=head
        c=0
        while(t!=None):
            c+=1
            t=t.next
        print(c)
        if c%2==0:
            print("even")
        else:
            print("odd")
    def length1(self):
         s=head
         f=head
         while f and f.next:
             s=s.next
             f=f.next.next
         if(f!=None):
            print("odd")
         else:
            print("even")

    
            
            
    
l=sll()
head=node(10)
head.next=node(20)
l.lastnode(30)
l.lastnode(40)
l.lastnode(50)
l.display()
print()
l.search(10)
l.middle()
#l.length()
l.length1()
#l.sum1()




