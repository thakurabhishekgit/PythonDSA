"""nums = [1,3,4,2,2]
print(nums[nums[0]])
def findDuplicate(nums):
    # Phase 1: Finding the intersection point in the cycle
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        
        if tortoise == hare:
            break

    # Phase 2: Finding the entrance to the cycle (duplicate number)
    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]
    
    return hare
x = findDuplicate(nums)
print(x)



#kadense algorithm 53
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

ma = nums[0]
sum = 0
for i in nums:
        if sum < 0:
            sum = 0
        sum += i
        ma = max(ma,sum)      
           
print(ma)



nums = [1,3,-1,-3,5,3,6,7]
k = 3
b = []
for i in range(0,len(nums)-2):
    m = max(nums[i:k])
    b.append(m)
    
    k = k + 1
print(b)    


nums = [1,2,3,4]
mul = 1
for i in range(0,len(nums)):
    if a[i]
    mul = mul*nums[i]
print(mul)

nums = [-1]
k = 1
final = 0
for i in range( len(nums) - 0):
    print(nums[i : k])
    avg = sum(nums[i : k]) / 1
    print(avg)
    final = max(final , avg)
    k = k + 1
print(final)      



#selection sort
nums = [10,2,5,3,67,8]
for i in range(len(nums)):
    min_index = i
    for j in range(i+1 , len(nums)):
        if nums[min_index] > nums[j]:
            min_index = j
    nums[i] , nums[min_index]  = nums[min_index] , nums[i]       
               

print("selection sort ",nums)


#bubble sort
nums = [10,2,5,3,67,8]
for i in range(0,len(nums) - 1):
    for j in range(len(nums) - 1):
        if nums[j] > nums[j+1]:
            temp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp
           
print(nums)     


def binary_search(arr, target):
    # Set initial low and high pointers
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        # Calculate the middle index
        mid = (low + high) // 2
        
        # Check if target is at mid
        if arr[mid] == target:
            return mid  # Target found at index mid
        # If target is greater, ignore left half
        elif arr[mid] < target:
            low = mid + 1
        # If target is smaller, ignore right half
        else:
            high = mid - 1
    
    return -1  # Target not found


arr = [1, 3, 5, 7, 9, 11]
target = 7

result = binary_search(arr, target)
if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")
     


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
#print(matrix[1][3]) # 1st row 3rd coloum
# 1 3 5 7
# 10 11 16 20  10 is mid
# 23 30 34 60
target = 3
row = len(matrix) #3
col = len(matrix[0]) # 4
low = 0
high = row * col - 1 # 11
while low <= high:
    mid = (low + high) // 2 # 0+11 // 2 = 5

    mid_value = matrix[mid // col][mid % col] # [mid // col = 5 // 11 = 1] phir [mid % col = 5 % 11 = 0] final = matric[1][0]
    if mid_value == target:
        print("found")   # Target found
    elif mid_value < target:
        low = mid + 1  # Search in the right half
    else:
        high = mid - 1 # 5 - 1 = 4


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:

                right = mid - 1
        
        return right  # `right` will be the floor of the square root
s = Solution()
print(s.mySqrt(8))



sentence = "hello hello world"   #The split() method splits the sentence into individual words, resulting in a list: ['hello', 'hello', 'world'].
unique_words = list(dict.fromkeys(sentence.split()))#dict.fromkeys() creates a dictionary where the keys are the words from the list, automatically removing duplicates because dictionary keys are unique.
#Example: dict.fromkeys(['hello', 'hello', 'world']) results in {'hello': None, 'world': None}.
print(" ".join(unique_words))
#The join() method combines the words in the list into a single string with spaces between them: "hello world".



sentence = "apple,banana,cherry"
words = sentence.split(",")  # Split using ',' as the delimiter
print(words)  # Output: ['apple', 'banana', 'cherry']


words = ['apple', 'banana', 'cherry']
sentence = ",".join(words)  # Combine with ',' as the separator
print(sentence)  # Output: "apple,banana,cherry"






class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Linked:
    def __init__(self):
        self.head = None 
    def display(self):
        t = self.head
        while(t!=None):
            print(t.data,"->",end=' ')
            t = t.next
    def add_at_end(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            t = self.head
            while(t.next!=None):
                t = t.next
            t.next = Node(data)  
    def add_at_start(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def add_at_posision(self,data , pos):
        new_node = Node(data)
        t = self.head
        for _ in range(pos - 1):
            t = t.next
        new_node.next = t.next
        t.next = new_node

    def delete_at_begin(self):
        temp = self.head
        self.head = temp.next    
        temp = None
    def delete_at_end(self):
        temp = self.head
        while temp.next.next != None:
            temp = temp.next
        temp.next = None    
    def delete_at_positions(self , position):
        temp = self.head
        for _ in range(position - 2):
            temp = temp.next
        temp.next = temp.next.next    
    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    
l1 = Linked()
l1.add_at_end(1)

l1.add_at_end(2)

l1.add_at_end(4)

l1.add_at_start(0)

l1.add_at_posision(3,3)

#l1.delete_at_begin()

#l1.delete_at_end()

#l1.delete_at_positions(3)

l1.reverse()


l1.display()                          


"""
