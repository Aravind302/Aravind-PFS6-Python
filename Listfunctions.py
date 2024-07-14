#List Functions
'''a=[7,8,9,45,623,14,0,47]
#max()
print(max(a))
#min()
print(min(a))
#sum()
print(sum(a))
#len()
print(len(a))
#all()
print(all(a))
#any()
print(any(a))
#sorted()
x=sorted(a)
print(a)
# Slicing
b=[85,3,2,4,5,6,9,7,8]
print(b)
print(b[:])
print(b[::])
print(b[::1])
print(b[0::1])
print(b[0:9:1])
print(b[5:])
print(b[3:7])    #here,3 is the index number and 7 is the position number
print(b[::4])
print(b[::-1])
print(b[-2:-6:-1])
  #Example:    find sum of indexed values of indexed even numbers
s = 0
for i in b[::2]:
    if i%2 == 0:
        s = s + i
print(s)

#Nested lists [Matrix Problems]
row = int(input())
col = int(input())
matrix = []
for i in range(row):
    x = list(map(int,input().split()))[:col]
    matrix.append(x)
print(matrix)
for i in matrix:
    print(*i,sep=" ")
    '''
#How to find duplicate element in present list
#Approach - 1
'''
n = int(input())
a = list(map(int,input().split()))[:n]
for i in a:
    if a.count(i)>1:
        print(i)
        break
'''
#Approach - 2
n = int(input())
a = list(map(int,input().split()))[:n]
for i in range(n):
    if a[i] in a[i+1:]:
        print(a[i])
        break
















    
