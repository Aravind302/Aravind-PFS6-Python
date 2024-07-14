#PATTERN PROBLEMS
#MODEL-1
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
#MODEL-2
    '''
1 
2 2 
3 3 3 
4 4 4 4 
'''
n= int(input())
for i in range(n):
    for j in range(i):
        print(i,end=" ")
    print()
        
#MODEL-3
'''
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 

'''
n=int(input())
a=0
for i in range(n,0,-1):
    a+=1
    for j in range(1,i+1):
        print(i,end=" ")
    print()
#MODEL-4
'''
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5
'''
n=int(input())
a=0
for i in range(n,0,-1):
    a+=1
    for j in range(1,i+1):
        print(a,end=" ")
    print()

#MODEL-5
    '''
1 
2 4 
3 6 9 
4 8 12 16 
5 10 15 20 25 
6 12 18 24 30 36 
7 14 21 28 35 42 49 
8 16 24 32 40 48 56 64 
'''
n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        suare=i*j
        print(i*j,end=" ")
    print()
    

















        
