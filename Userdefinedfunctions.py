#User-defined Functions
# way to long word (problem)
#approach-1 (normal method)
'''
T=int(input())
for i in range(T):
    s=input()
    if len(s) <= 10:
        print(s)
    else:
        res = ""
        res = res + s[0]
        res = res + str(len(s)-2)
        res = res + s[-1]
        print(res)
        '''
#Approach-2 (with parameter with return type)
'''
def my(s):
    if len(s)<=10:
        return s
    else:
        res=""
        res=res+s[0]
        res=res+str(len(s))
        res=res+s[-1]
        return res
t=int(input())
for i in range(t):
    x = input()
    print(my(x))
    '''
#Approach-3 (with parameter without return type)
'''
def my(s):
    if len(s)<=10:
        print(s)
    else:
        res=""
        res=res+s[0]
        res=res+str(len(s))
        res=res+s[-1]
        print(res)
t=int(input())
for i in range(t):
    x = input()
    my(x)
    '''
#Approach-4 (without parameter with return type)
'''
def my():
       s = input()
       if len(s)<=10:
           return s
       else:
            res=""
            res=res+s[0]
            res=res+str(len(s))
            res=res+s[-1]
            return res
t=int(input())
for i in range(t):
    print(my())
'''
#Approach-5 (without parameter without return type)
'''
def my():
       s = input()
       if len(s)<=10:
           print(s)
       else:
            res=""
            res=res+s[0]
            res=res+str(len(s))
            res=res+s[-1]
            print(res) 
t=int(input())
for i in range(t):
    my()

'''
#Function arguments
#1.Default Arguments

def fun(a=10,b=20):
    print(a+b)
fun()
fun(20)
fun(100,200)

#Required Arguments

def fun(a,b):
    print(a+b)
#fun()
#fun(20)  these both of two shows error called type error because of these argument wants two values but we given one value
fun(100,200)
#Keywords arguments

def fun(a=10,b=20):
    print(a+b)
fun()
fun(a=20)

#Varibale number of arguments

def fun(*x):
    res = 123
    for i in x:
        res = res - i
    print(res)
fun()
fun(2,3,56, 45)
fun(41,56)

def my(*a):
    for i in a:
        print(i)
my("hello","Aravind","welcome","to","my","page")







































    
