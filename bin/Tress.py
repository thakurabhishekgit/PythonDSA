class Node:
    def __init__(self,x):
        self.data = x
        self.right = None
        self.left = None

def search(root,x):
    if(root==None):
        return "notFound"
    if (root.data==x):
        return "found"
    elif (x<root.data):
        return search(root.left,x)
    else:
        return search(root.right,x)
def inorder(root):
    if(root==None):
        return 
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)           
def preorder(root):
    if(root==None):
        return 
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)
def postorder(root):
    if(root==None):
        return 
    postorder(root.left)
    postorder(root.right)
    print(root.data,end = " ")
def insert(root,x):
    if(root== None):
        return Node(x)
    if(x<root.data):
        root.left = insert(root.left,x)
    else:
        root.right = insert(root.right,x)    

def add_all(root):
    
    if(root== None):
        return 0
    else:
        return root.data+add_all(root.left)+add_all(root.right) 
    
def height(root):
           if root==None:
               return -1
           else:
               lh=height(root.left)
               rh=height(root.right)
           return max(lh,rh) + 1

def printall(root):
            if root==None:
               return 
            print(root.data)
            printall(root.left)
            printall(root.right)

def insert(root, x):
    if root is None:
        root = Node(x)
        return
    else:
        
        
        if x < root.key:
            if root.left:
                insert(root.left, x)
                return
            root.leftBranch = Node(x)
            return
        
        if root.rightBranch:
            insert(root.right, x)
            return
        root.right = Node(x)
def height(root):
           if root==None:
               return -1
           else:
               lh=height(root.left)
               rh=height(root.right)
           return max(lh,rh) + 1
def balance(root):
    if root==None:
        return 0
    lh=height(root.left)
    rh=height(root.right)
    if abs(height(root.left)-height(root.right))<=1:
        print("balance")
    else:                                                                                 #   10
        print("not balance")                                                           #   5        15
                                                         #                              2      7        200
def heavy(root):                                                    #    
    if root==None:
        return 0
    if abs(height(root.left)>height(root.right)):
        
        print("left heavy")
    elif abs(height(root.left)==height(root.right)):
        print("equally heavy")
    else:
        print("right heavy")   

def mul(root):
    if root==None:
        return 1
    else:
        return root.data*mul(root.left)+mul(root.right)

def search (root,x):
    if(root==None):
        return "notFound"
    if (root.data==x):
        return "found"
    elif (x<root.data):
        return search(root.left,x)
    else:
        return search(root.right,x)
    
def insert(root,x):
    if(root== None):
        return Node(x)
    if(x<root.data):
        root.left = insert(root.left,x)
    else:
        root.right = insert(root.right,x)
    return root
    

def add_even(root):
    if root==None:
        return 0
    if root.data%2==0:
        return root.data+add_even(root.left)+add_even(root.right)
    else:
        return add_even(root.left)+add_even(root.right)
        

root = Node(10)
root.left = Node(5)    
root.right = Node(15)  
root.left.left = Node(2)  
root.left.right = Node(7) 
insert(root.right.right,200)

printall(root)
print(search(root,5))
print("INORDER : ")
print(inorder(root))
print("PREORDER : ")
print(preorder(root))
print("POSTORDER : ")
print(postorder(root))

print(add_all(root))

print(balance(root))
print(heavy(root))
print(height(root))
print(mul(root))






















