'''
ip:
5
1.word
1.word
3.wo
4.word
2word
op:
1--->no of words start with wo in above list only 1 so output is 1 
false
1--->insert the word
2--->complete word should be checked
3---->prefixed should be checked
in this code take input like this
ip:3
1 word
2 word
True
3 wo
True
using tries'''
'''ip: for case 4
7
1 word
1 words
1 worlds
1 wor
1 apple
1 wood
4 wor
wor
word
words
worlds
'''
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
    def print_all_prefix(self,str):
        def fun(t,s):
            if t.flag==1:
                print(s)
            for i in t.d:
                fun(t.d[i],s+i)#sending next node
            
        t=self.root
        s=""
        for i in str: #war w,o,r
           if i in t.d:# go to w then w's trie is o and o's trie is r
               s=s+i
               t=t.d[i]#now iam at postion r
           else:
                return 
        fun(t,s)#t=r
    

        
               
                
t1=tries()      
n=int(input())
for i in range(n):
    a,s=input().split() # a is number and s is string
    if a=='1':
        t1.insert(s)
    if a=='2':
        print(t1.search(s))
    if a=='3':
        print(t1.prefix(s))
    if a=='4':
        t1.print_all_prefix(s)