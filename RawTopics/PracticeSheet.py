"""class Node:
    def  __init__(self, data):
        self.data = data
        self.next = None
        self.prev=None
class dll:
    def __init__(self):
        self.head = None
        self.tail = None
    def add_back(self,x):
        if self.head == None:
            self.head = Node(x)
            self.tail =  self.head
        else:
            n = Node(x)
            self.tail.next = n
            n.prev = self.tail
            self.tail = n
    def display(self):
        if self.head == None:
            print("Empty")
        else:
            t = self.head
            while(t!=None):
                print(t.data,end="<->")
                li.append(t.data)
                t = t.next    
            x = sorted(li)
            print()
            print("sorted data is : ")
            for i in range(len(x)):
                print(x[i],end=" ")

    def Sorted(self):
            if self.head == None:
               print("Empty")
            else:
                a = self.head
                b = a.next.data
            while(a!=b):    
                if a.data > b.next.data:
                    print(a.data)
                    a = a.next
                    b = a.next
                else:
                    print("a")   
                      

li=[]
a = dll()
a.add_back(9)
a.add_back(3)                
a.add_back(5)   
a.add_back(10)
a.add_back(12)
a.add_back(8)   
a.display()  """      


"""class Node:
    def __init__(self,x):
        self.data = x
        self.right = None
        self.left = None
def Insert(root,x): 
    if root is None: 
        root = Node(x)
    if x < root.data:
        if root.left is None:
           root.left = Node(x)
        else:
           root.left = Insert(root.left,x)
    else:
        if root.right is None:
            root.right = Node(x)
        else:
            root.right = Insert(root.right,x)
def insert(root,x):
    if(root== None):
        return Node(x)
    if(x<root.data):
        root.left = insert(root.left,x)
    else:
        root.right = insert(root.right,x)      
def inorder(root):
    if(root==None):
        return 
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)                    

root = Node(10)
Insert(root,1)
Insert(root,4)
Insert(root,6)
Insert(root,99)
print(inorder(root))




class Tree: 
  
    def __init__(node, value): 
        node.value = value  
        node.left = None
        node.right = None
    
    def Inorder( node, Root ): 
        if( Root is None ): 
            return
        node.Inorder(Root.left) 
        print(Root.value,end = ' ') 
        node.Inorder(Root.right) 
  
    def Insert(node, value): 
        if node is None: 
            node = Tree(value)
        elif value < node.value:
            if node.left is None:
                node.left = Tree(value)
            else:
               node.left.Insert(value) 
        else:
            if node.right is None:
                node.right = Tree(value)
            else:
                node.right.Insert(value)
    def preorder(node,Root):
        if( Root is None ): 
            return
        print(Root.value,end = ' ') 
        node.Inorder(Root.left) 
        node.Inorder(Root.right)

Root = Tree(6) 
l = [10,20,3,4,5,100,200]
for i in l:
    Root.Insert(i)

print ("Inorder traversal after insertion: ",end = '')
Root.Inorder(Root)
print ("pre traversal after insertion: ",end = '')
Root.preorder(Root)
"""


from collections import deque

def bfs(graph , start):
    visited = set()
    queue = deque([start])
    result = []
    while queue:
        node  = queue.popleft()
        if node not in visited:
            visited.add(node)
            result.append(node)
            queue.extend(graph[node])
    return result
def dfs(graph , start):
    visited = set()
    result = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            result.append(node)
            stack.extend(graph[node])
    return result 

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}   

print(dfs(graph, 'A'))


