# word suggestion,autocorrect are applications of tries
class node:
    def __init__(self):
        self.d={}
        self.flag=0
class tries:
    def __init__(self):
        self.root=node()#creation of root node
    def insert(self,str1):#str=word
        t=self.root
        for i in str1:#i=w,0,r,d...
            if i not in t.d:#intially
                t.d[i]=node()# i is w node()is reference trie
            t=t.d[i]#already there move to next iteration node
        t.flag=1
    def search(self,str1):
        t=self.root
        for i in str1:
            if i not in t.d:
                return False
            t=t.d[i]#going to next palce if found
        if t.flag==1:
            return True
        else:
            return False
    def prefix(self,str1):
        t=self.root
        for i in str1:
            if i not in t.d:
                return False
            t=t.d[i]
        return True
               
                
        
        
t1=tries()
t1.insert("word")
print(t1.search("word"))
print(t1.prefix("wo"))

        