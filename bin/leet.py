"""import json
a = json.loads(input())
b=[]
k=int(input())
for i in range(1,100):
    if i in a:
        continue
    else:
        b.append(i)
print(b[k-1])        







Input: arr = [2,3,4,7,11], k = 5nums = 
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9."""


"""lis = [1,2,3,4,1,2]

uniqueList = []
duplicateList = []

for i in lis:
	if i not in uniqueList:
		uniqueList.append(i)
	elif i not in duplicateList:
		duplicateList.append(i)

print(duplicateList)"""







"""nums = [0,1,2,2,3,0,4,2]
val = 2
a=[]
for i in range(len(nums)):
    if nums[i]==2:
        continue
    else:
        a.append(nums[i])
print(a)
print(len(a))   """     


"""n = [1,3,5,6]
a = 1

for i in range(len(n)):
    if a < n[i] or n[i]==a:
        print(i)
        break"""
a = [9]

"""for i in range(len(a)):
    if i==len(a)-1:
        a[i] = a[i]+1
        
        if i==len(a)-1 and a[i]>9:
            s = str(a[i])
            print(s[])
            for i in range(len(s)):
                t = int(a[i-1])
                print(t)"""


"""a = [1,2,3,0,0,0]
b = [2,5,6]
c = sorted(a+b)
f = []
for i in range(len(c)):
    if c[i]==0:
        continue
    else:
        f.append(c[i])

print(f)        """





"""class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        l=[]
        for i in digits:
            x=i
            if(x!=digits[-1]):
                l.append(x)
            else:
                x=i+1
                x=str(x)
                for i in x:
                    l.append(int(i))
        return l"""




l = [10,20,30,40]
f = l[0:-1]
l = l[3:4]
for i in f:
    l.append(i)
print(l)

