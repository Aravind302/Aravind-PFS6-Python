#Recursion - 1  (printing 10 to 1)
'''
def cal(n):
    if n >= 1:
        print(n)
        cal(n-1)
cal(10)

def calc(a):
    if a<=12:
        print(a)
        calc(a+1)
        
calc(1)
'''
#Recursion - 2
'''
import sys
sys.setrecursionlimit(2000)
def calc(n):
    print(n)
    calc(n+1)
calc(1)
'''
#Recursion - 3
#While Loop
'''
n = int(input())
while n > 1:
    if n%2 == 0:
        print(n)
    n = n - 1
'''
#Recursion
'''
def name(n):
    if n > 1:
        if n%2 == 0:
            print(n)
        name(n-1)
    else:
        return
name(10)

'''
#Recursion - 6
#While Loop
'''
t = int(input())
while t > 0:
    x = int(input())
    if x%2 == 0:
        print("even")
    else:
        print("Odd")
    t = t - 1
 '''   
#Recursion - 2

def recr(t):
    if t == 0:
        return
    else:
        n = int(input())
        if n%2==0:
            print("Even")
        else:
            print("Odd")
    recr(t-1)

t = int(input())
recr(t)



























