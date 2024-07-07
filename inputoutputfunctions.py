#input functions
'''x=input()
print(x)
print(type(x))
y=int(input())
print(y)
print(type(y))'''
#method-1
'''x=input().split()
print(x)
print(type(x))
y=input().split(",")
print(y)
print(type(y))'''
#method-2
'''x,y= map(int,input().split())
print(x)
print(type(x))
print(y)
print(type(y))'''
#method-3
'''a=list(map(int,input().split()))
print(a[1])
print(type(a[1]))'''
#method-4
'''a=tuple(map(float,input().split()))
print(type(a))
print(type(a[0]))
print(a[0])'''
#method-5
'''a=set(map(int,input().split()))
print(type(a))
print(a)'''
#EXAMPLE-1
#approach-1
'''name=input("enter your name:")
mobile=int(input("enter your mobile number:"))
email=input("enter your email id:")
print(name)
print(mobile)
print(email)'''
#approach-2
'''name=input("enter your name: \n")
mobile=int(input("enter your mobile number: \n"))
email=input("enter your email id: \n")
print(name)
print(mobile)
print(email)'''
#approach-3
'''print("enter your name:")
name=input()
print("mobile no.")
mobile=int(input())'''


#output formating
#case-1
'''name=input("Enter your name:")
age=int(input("Enter your age:"))
print(name)
print(age)
#Method-1
#using comas(,)
print("my name is",name,".",age,"is my age")
#Method-2
#.format
print("my name is {} . {} is my age".format(name,age))
#Method-3
#f-format
print(f"my name is {name} . {age} is my age")'''
#case-2
# if we want two digits or 8 digits after the decimal point,then we will use method called (.foramt).
b=12.5689746564120025655200
print("my number is {:.2f}".format(b))
print("my number is {:.8f}".format(b))
#Task-1
fname,lname=input("Enter your name[fname-lname]: ").split("-")
height1,height2=(input("enetr your height:").split("-"))
age=int(input("eneter your age:"))
salary=float(input("enetr your salary:"))
print("First name:{}".format(fname))
print("Last name:{}".format(lname))
print(f"Height: {height1+ "."+height2}")
print("Age:{}".format(age))
print("salary:{:.3f}/-".format(salary))
































