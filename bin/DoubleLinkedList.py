class Node:
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
                t = t.next    
    def displayrev(self):
        if self.head == None:
            print("none")
        else:
            t=self.tail
            while(t!=None):
                print(t.data,end="<->")
                t = t.prev 
    def  lengtheoro(self):
        if self.head == None:
            print("none")
        else:
            l = 0
            t=self.tail
            while(t!=None):
                l = l + 1
                t = t.prev 
        if l%2==0:
            print("even")
        else:
            print("odd")    
    def addall(self):
        if self.head == None:
            print("none")
        else:
            sum = 0
            t=self.head
            while(t!=None):
                sum = sum + t.data
                t = t.next
            print("sum of nodes",sum)    

    def mid(self):
 
        
        if self.head == None:
            print("Empty")
        else:
            a = self.head
            b = self.tail 
            while(a!=b and a.next!=b):
                
                a = a.next
                b = b.prev
            print("mid element :",b.data)   
                
    def pal(self):
 
        
        if self.head == None:
            print("Empty")
        else:
            a = self.head
            b = self.tail
            while(a!=b):
                if(a.data==b.data):
                    
                    a = a.next     
                    b = b.prev
                      
                else:
                    print("no")
                    return
            print("pal")
                           
                       






l1 = dll()
l1.add_back(10)
l1.add_back(20)
l1.add_back(30)
l1.add_back(20)
l1.add_back(10)

l1.pal()

l1.display()
print(" ")
l1.displayrev()
print(" ")
l1.lengtheoro()
print(" ")
l1.addall()
l1.mid()
print(" ")
l1.pal()
