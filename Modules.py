#Built-in modules
'''
import random
x=random.randint(32,99)
print(x)
#User-defined functions
import sample1
import sample2
print(sample1.x)
print(sample2.z)
sample1.hello()
sample2.my()
'''
# files
#read()
'''
f=open("akki.txt","r")
print(f.read())
f.close()
'''

# write()
'''
f=open("hello.txt","w")
f.write("I completed my graduation in the year 2024")
f.close()
'''
#append()
'''
f=open("hello.txt","a")
f.write("mechanical branch")
f.close()
'''
#read and write
f= open("Akki.txt","r+")
f.write("I am from karimnagar")
f.seek(0)
print(f.read())
f.close()
