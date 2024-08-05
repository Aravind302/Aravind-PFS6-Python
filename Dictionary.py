#Dictionary
'''
#creating an empty dictionary
d1={}
print(d1)
print(type(d1))
#Creating dictionaries with hetrogenous values 
d={1:"akki",2:"aravind",3:23,4:4.52}
print(d)
print(type(d))
#Creating dictionaries with homogeneous values (input from user)
d={}
for i in range(4):
    key=input("key:")
    values=input("value:")
    d[key]= values
print(d)
'''
'''
#Accessing elements in a dictionary
#we can access the elements in 3 different ways they are:
#1.By indexing
d1={1:"akki",2:"aravind",3:23,4:4.52}
a=d1[3]
print(a)
b=d1[2]
print(b)
#2.By Buit-in Methods [get()]
c=d1.get(4)
print(c)
d=d1.get(2)
print(d)
#3.By using For loop
for i in d1:
    print(i,d1[2])
#Modification dictionary
d1[1]="moluguri"
print(d1)
#Insertion into Dictionary
d1[5] = 51
print(d1)
#deleting a dictionary
del d1[3]
print(d1)
del d1
print(d1) #if we print again d1 after deleting it shows an error called name error

'''
# Methods in Dictionaries
#1.get()
d={1:"akki",2:"aravind",3:23,4:4.52}
a=d.get(2)
print(a)
b=d.get(3)
print(b)
#2.update()
d1={10:50,20:10,30:23,40:4.52}
d1.update(d)
print(d1)
#3.copy()
d2=d.copy()
print(d2)
#4.pop()
d.pop(2)
print(d)
d1.pop(40)
print(d1)
#5.popitem()
d.popitem()
print(d)
d.popitem()
print(d)
d1.popitem()
print(d1)
d1.popitem()
print(d1)
#6.clear()
d1.clear()
print(d1) # it will shows an empty list
#7.key()
d2={1:"akki",2:"aravind",3:23,4:4.52}
print(d2.keys())
#8.values()
print(d2.values())
#9.item()
print(d2.items())
#10.fromkeys()
print(dict.fromkeys(d2,5))
print(dict.fromkeys(d2,120))
#Setdefault()
print(d2.setdefault(5))
print(d2)
print(d2.setdefault(6,56000))
print(d2)

# Sample Program 1( Given string is pangram or not)
s="the quick brown fox jumps over the lazy dog"
s1="qwertyuioplkjhgfdsazxcvbnm"
d={}
for i in s:
    if i in s1:
        if i not in d:
            d[i]=1
if len(d)==26:
    print("pangram")
else:
    print("not pangram")


# Sample program 2 ( Given a string of charcters, find the first repeating character)   

string = "aravind"
count = {}
for i in string:
    if i in count:
        print(i)
        break
    count[i]=1
else:
    print("No repeating character  is found.")












