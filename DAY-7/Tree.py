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
            if root.right:
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
    
t1=tree()
root=t1.create(30)
t1.insert(root,15)
t1.insert(root,35)
t1.insert(root,8)
t1.insert(root,5)
print("the preorder traversal:")
t1.preorder(root)
print()
print("the inorder traversal:")
t1.inorder(root)
print()
print("the postorder traversal:")
t1.postorder(root)
    
