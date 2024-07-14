# Leet coode problems(3190)
'''You are given an integer array nums. In one operation, you can add or subtract 1 from any element of nums.
   Return the minimum number of operations to make all elements of nums divisible by 3.
Example 1:

Input: nums = [1,2,3,4]

Output: 3'''
nums = [1,2,3,4]
s = 0
for i in nums:
    if (i%3 != 0):
        s = s + 1
print(s)
#1512 leetcode problem
n=[1,2,3,1,1,3]
s=0
for i in range(len(n)):
    if n[i] in n[i+1:]:
        x=n[i+1:].count(n[i])
        s=s+x
print(s)
    
#2011 leetcode problem
x=["X++","++X","--X","X--"]
s=0
for i in x:
    if "++" in i:
        s=s+1
    else:
        s=s-1
print(s)
#1672 leetcode problem
x=[[1,2,3],[3,2,1]]
res=[ ]
for i in x:
    res.append(sum(i))
print(max(res))
#1470 leetcode problem
# Approach-1
nums=[2,5,1,3,4,7]
n=3
res=[]
for i in range(n):
    res.append(nums[i])
    res.append(nums[n+i])
print(res)
# Approach-2
nums=[1,2,3,4,4,3,2,1]
n=4
res=[]
r1=nums[n:]
for i in range(n):
    res.append(nums[i])
    res.append(r1[i])
print(res)


















