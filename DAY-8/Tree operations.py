'''left subtree height -right sub tree'''
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root=None
        
    def create(self,data):
        if(self.root==None):
            self.root=node(data)
            return self.root
        
        
    def insert(self,root,data):
        if data>root.data:
            if root.right!=None:
                self.insert(root.right,data)
            else:
                root.right=node(data)
        if data<root.data:
            if root.left:
                self.insert(root.left,data)
            else:
                root.left=node(data)
                
                
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data,end=" ")
            self.inorder(root.right)
            
            
    def preorder(self,root):
        if root:
            print(root.data,end=" ")
            self.preorder(root.left)
            self.preorder(root.right)
            
            
    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data,end=" ")
            
            
    def sum1(self,root):
        if root is None:
            return 0
        return root.data + self.sum1(root.left) + self.sum1(root.right)
    def ls(self,root):
        if root is None:
            return 0
        return root.data + self.sum1(root.left) + self.sum1(root.right)
    def rs(self,root):
        if root is None:
            return 0
        return root.data + self.sum1(root.left) + self.sum1(root.right)
    
    def esum(self,root):
        if root==None:
            return 0
        else:
            esum=0
            if root.data%2==0:
                esum=esum+root.data
            esum+=self.esum(root.left)
            esum+=self.esum(root.right)
        return esum
    
    def odsum(self,root):
        if root==None:
            return 0
        else:
            esum=0
            if root.data%2!=0:
                esum=esum+root.data
            esum+=self.odsum(root.left)
            esum+=self.odsum(root.right)
        return esum
    
    def Even_Odd_Diff(self,root):
        if root==None:
            return 0
        es=0
        if root.data%2==0:
            es=es+root.data
        else:
            es=es-root.data
        es+=self.Even_Odd_Diff(root.left)
        es+=self.Even_Odd_Diff(root.right)
        return es
    def height(self,root):
        if root==None:
            return -1 #height of None is -1
        
        l=self.height(root.left)
        r=self.height(root.right)
        h=max(l,r)+1
        return h
    
    def bal(self,root):
        return abs(self.height(root.left)-self.height(root.right))<=1
    
    def no_of_leaf_nodes(self,root):
        c=0
        if root==None:
            return 0
        if root.left==None and root.right==None:
            print(root.data)
            c=c+1
            
        c+=self.no_of_leaf_nodes(root.left)
        c+=self.no_of_leaf_nodes(root.right)
        return c
    def sum_leaf(self,root):
        s=0
        if root==None:
            return 0
        if root.left==None and root.right==None:
            s=s+root.data
        s+=self.sum_leaf(root.left)
        s+=self.sum_leaf(root.right)
        return s
    
    def search(self,root,x):
        if root==None:
            return False
        if root.data==x:
            return True
        if x>root.data:
            return self.search(root.right,x)
        else:
           return self.search(root.left,x)
        
    def depth(self,root,x,c):
        if root==None:
            return -1
        if root.data==x:
            return c
        if root.data>x:
            return self.depth(root.left,x,c+1)
        else:
            return self.depth(root.right,x,c+1)
            
            
                
            

    
                
                

            
    
t1=tree()
root=t1.create(30)
t1.insert(root,15)
t1.insert(root,35)
t1.insert(root,8)
t1.insert(root,5)

print("preorder traversal is:")
t1.preorder(root)
print()
print("inorder traversal is:")
t1.inorder(root)
print()
print("postorder traversal is:")
t1.postorder(root)
print()
print("the sum of all the nodes are:")
print(t1.sum1(root))
print("the left subtree sum is:")
print(t1.ls(root.left))
print("the even right subtree sum is:")
print(t1.rs(root.right))
print("the even sum is:")
print(t1.esum(root))
print("the odd sum is:")
print(t1.odsum(root))
print("even odd difference is:")
print(abs(t1.Even_Odd_Diff(root)))
print("the height of the tree is:")
print(t1.height(root))
print("the tree is:")
if(t1.bal(root)):
   print("balenced")
else:
    print("not balenced")
print("the total number of leaf nodes are:")
print(t1.no_of_leaf_nodes(root))
print("sum of leaf")
print(t1.sum_leaf(root))
print("search element in the tree is:")
r=t1.search(root,45)
if r==1:
    print("found")
else:
    print(" not found")
print("the depth of tree from particular node is:")
print(t1.depth(root,5,0))



























    


