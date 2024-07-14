


#LISTS
#List Declaration
'''
x=[12,23.5,56,789,78]
print(x)
x=[45,45,63.25,"sai",True,False,45]
print(x)
x=list(map(int,input()))
print(x)

x=list(map(int,input().split()))
print(x)
'''
#Accessing
#Indexing
#positive indexing
x=[45,12,46,78,23.6]
print(x)
print(x[2])
print(x[3])
print(x[0])
#Negative indexing
x=[45,12,46,78,23.6]
print(x)
print(x[-2])
print(x[-3])
print(x[-5])
#looping
#For loop with range()
x=[45,78,236,73,36,89,41]
for i in range(7):
   print(x[i],end="_")
print()
#For loop without range()
x=[45,78,236,73,36,89,41]
for i in x:
    print(i,end="_")
print()

#Kwargs
x = [12,23,34,45,56,67]
print(x)
print(*x)
print(*x,sep=" ")
print(*x,sep="_")





