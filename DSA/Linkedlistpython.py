class Node:
    def __init__(self,x):
        self.data = x
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    
    def Display(self):
        t = self.head
        while (t!= None):
            print(t.data,"->",end='')
            t = t.next
    def Add_back(self,x):
        if(self.head == None):
            self.head = Node(x)
        else: 
            t = self.head
            while(t.next!=None):
                t = t.next
            t.next = Node(x)
    def Add_beg(self,x):
        t = Node(x)
        t.next = l1.head
        l1.head = t   
    def add_all(self):
        t = self.head
        sum = 0
        while (t!= None):
            sum = sum + t.data
            t = t.next
        print("Sum of all the nodes",sum)
    def sum_odd_all(self):
        t = self.head
        even = 0
        odd = 0
        while(t!=None):
            if (t.data%2==0):
                even = even + t.data
            else:
                odd = odd + t.data    
        print("diff")
        diff = even - odd
        print(diff)
    def Displaylen(self):
        t = self.head
        len = 0
        while (t!= None):
            print(t.data,"->",end='')
            len = len + 1
            t = t.next            
        print("lenth is :",len)
        if (len==7):
            mid = 7//2
            print(mid)
            t = self.head
        for i in range(mid):
            t = t.next
        print(t.data)    




l1=LinkedList()
l1.Add_back(10)
l1.Add_beg(20)
l1.Add_beg(23)
l1.Add_beg(30)
l1.Add_beg(70)
l1.Add_beg(80)
l1.Add_beg(350)


print(" ")
l1.Displaylen()





"""while(1):
    print("Enter your choice")
    print("1.add_back\n2.add_beg\n3.display\n4.add_all")
    c=int(input())
    match c:
        case 1 :
             a=int(input("Enter a number tobe added at beg"))
             l1.Add_back(a)
        case 2:
            a=int(input())   
            l1.Add_beg(a)  
        case 3 : 
            l1.Display()
        case 4 :
            l1.add_all()    """
