#if statement
'''n=int(input())
if n%2==0:
    print("{} is even".format(n))
print("{} is number".format(n))'''
#if else statement
#Type-1
'''n=int(input("number:"))
if n>0:
    print("true")
else:
    print("negative")
#Type-2
marks=int(input())
if marks>=35:
    print("pass")
    print("congrats")
else:
    print("fail")
    print("sorry")'''
#elif statement    
'''n=int(input("number:"))
if n%2==0:
    print("even")
elif n%1==0:
    print("odd")
else:
    print("number")'''
#nested if statements
n=int(input("number:"))
if n%2==0:
    if n>0:
        print("positive even number")
    else:
        print("negative even number")
        if(n<0):
            print("Positive odd number")
        else:
            print("Negetive odd number")
else:
    print("false")
