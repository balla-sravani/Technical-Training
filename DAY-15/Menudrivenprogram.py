'''
ip:
7
1 school
1 world
1 word
1 scholor
2 word
2 wood
3 sch
4 word
op:
True
false
True
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
4---->remove that word from the list

'''
def add(e,l):
    l.add(e)
    print(l)

def search(e,l):
    for i in l:
        if i==e:
            print("True")
            break
    else:
        print("False")
def prefix(e,l):
    c=0
    for i in l:
        if e in i:
            c=c+1
            break
    print(c)
    
def pop(e,l):
    l.remove(e)

    
n=int(input())
l=set()
while(n):
    choice=0
    choice=int(input("enter your choice"))
    if choice==1:
        e=input("enter the string")
        add(e,l)
    if choice==2:
        e=input("enter the choice to be search")
        search(e,l)
    if choice==3:
        e=input("enter the choice to be prefix")
        prefix(e,l)
    if choice==4:
        e=input("enter the choice to remove")
        pop(e,l)
        
       


















                
                
            
            
    
