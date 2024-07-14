#Symbolic Patterns
#Type-1

'''
* * * * 
* * * * 
* * * * 
* * * *'''

for i in range(4):
    for j in range(4):
        print("*",end=" ")
    print()
#Type-2
'''
# 
# # 
# # # 
# # # # 
# # # # # 
# # # # # # 
# # # # # # # 
# # # # # # # # '''

for i in range(8):
    for j in range(8):
        if j<=i :
            print("#",end=" ")
    print()
#Type-3
    '''
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* '''
for i in range(6):
    for j in range(6):
        if i<=j:
            print("*",end=" ")
    print()
        
#Numeric Patterns
#Type-1
#Appproach-1
    '''
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5 
'''
x=1
for i in range(6):
    for j in range(6):
        print(x,end=" ")
    x=x+1
    print()
    
#Approach-2
for i in range(6):
    for j in range(6):
        print(i+1,end=" ")
    print()
#Approach-3
for i in range(1,7):
    x=str(i)+" "
    print(x*6)
#Type-2
    '''
1 2 3 
4 5 6 
7 8 9 
'''
x=1
for i in range(3):
    for j in range(3):
        print(x,end=" ")
        x=x+1
    print()
#Type-3
    '''
# # # # # 
1 2 3 4 5 
# # # # # 
1 2 3 4 5 
# # # # #
'''
x=1
for i in range(5):
    for j in range(5):
       if i%2==0:
           print("#",end=" ")
       else:
           print(x,end=" ")
           x=x+1
    x=1
    print()
#Type-4
'''
# # # # # # # # # # 
# @ @ @ @ @ @ @ @ # 
# @ @ @ @ @ @ @ @ # 
# @ @ @ @ @ @ @ @ # 
# @ @ @ @ @ @ @ @ # 
# @ @ @ @ @ @ @ @ # 
# @ @ @ @ @ @ @ @ # 
# @ @ @ @ @ @ @ @ # 
# @ @ @ @ @ @ @ @ # 
# # # # # # # # # # 
'''
n=int(input())
for i in range(n):
    for j in range(n):
        if (i==0 or j==0 or i==n-1 or j==n-1):
            print("#",end=" ")
        else:
            print("@",end=" ")
    print()



#SOME PATTERN PROBLEMS
# MODEL-1
'''
# # 
# # # 
# # # # 
# # # # # 
# # # # # 
# # # # 
# # # 
# # 
# 

'''
for i in range(5):
    for j in range(5):
        if i>=j:
            print("#",end=" ")
    print()
for i in range(5):
    for j in range(5):
        if i<=j:
            print("#",end=" ")
    print()

# MODEL-2
'''
# # # # # # # # 
1 2 3 4 5 6 7 8 
# # # # # # # # 
1 2 3 4 5 6 7 8 
# # # # # # # # 
1 2 3 4 5 6 7 8 
# # # # # # # # 
1 2 3 4 5 6 7 8 
'''
n= int(input())
for i in range(n):
    for j in range(n):
        if i%2==0:
            print("#",end=" ")
        else:
            print(x,end=" ")
            x=x+1
    x=1        
    print()
    
# MODEL-3
'''
# # # # # # # # # # 
#                 # 
#                 # 
#                 # 
#                 # 
#                 # 
#                 # 
#                 # 
#                 # 
# # # # # # # # # # 
'''
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print("#",end=" ")
        else:
            print(" ",end=" ")
    print()
   




    
