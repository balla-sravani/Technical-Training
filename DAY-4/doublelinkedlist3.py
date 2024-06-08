'''binary search cannot be possible in linked list'''
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
        while(t!=s and t!=s.next):
            t = t.next
            s = s.prev
            if t==s:
                f=1
                break
        if f==1:
            print("odd")
        else:
            print("even")
    def palindrome(self):
        t=self.head
        t1=self.tail
        f=0
        while(t!=t1 and t!=t1.next):
            if(t.value==t1.value):
                t=t.next
                t1=t1.prev
            else:
                f=1
                break
        if(f==1):
            print("not palindrome")
        else:
            print("palindrome")
    def sorting(self):
        slow=self.head
        fast=self.head
        while(fast!=None):
            slow=slow.next
            fast=fast.next.next
        t=self.head
        t1=slow
        while(t!=t1 and t1!=None):
            t.value,t1.value=t1.value,t.value
            t1=t1.next
            t=t.next
    '''def rotate(self):
        t=self.head
        t1=self.head.next
        t3=None
        while(t!=None and t1!=None):
            if t==self.head:
                t.next=t1.next
                t1.next=t
                t1.prev=t3
                t.prev=t1
                head=t1
                t,t1=t1,t
                t=t1.next
                t1=t.next
            else:
                t.next=t1.next
                t1.next=t
                t1.prev=t3
                t.prev=t1
                t3.next=t1
                t,t1=t1,t
                t3=t1
                t=t1.next
                t1=t.next'''
    def eosum(self,t,s,s1):
        if t==None:
            return abs(s-s1)
        if(t.value%2==0):
            s=s+t.value
        else:
            s1=s1+t.value
        return self.eosum(t.next,s,s1)
    def prime(self,t,c):
        if t==None:
            return c
        def pnt(s,n):
            if(s>=(n//2)+1):
                return 1
            if n%s==0:
                return 0
            return pnt(s+1,n)
        if(pnt(2,t.value)):
            c=c+1
        return self.prime(t.next,c)
                
        
                    
        
        
            
        
    

    
                
            
            
l=dll()
l.insert_Begin(10)
l.insert_End(2)
l.insert_End(30)
l.insert_End(7)
l.insert_End(5)
l.insert_End(60)
l.traverse()
l.rev()
print() 
l.linearsearch(50)
l.length()
l.palindrome()
l.sorting()
l.traverse()
x=l.eosum(l.head,0,0)
print(x)
y=l.prime(l.head,0)
print(y)

