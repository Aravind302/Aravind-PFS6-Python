# normal Approach by using function
def add(a,b):
    return a+b
print(add(42,18))

# lambda functions

add=lambda a,b : a+b
print(add(12,12))

#lambda with filter

lst=[1,2,3,5,6,7,8,9]
das=list(filter(lambda a:a%2==0,lst))
print(das)

lst=[1,2,3,5,6,7,8,9]
saw=list(filter(lambda a:a%2!=0,lst))
print(saw)

#lambda with map

lst1=[1,2,3,5,6,7,8,9]
fad=list(map(lambda a:a**2,lst1))
print(fad)

lst2=[9,99,199,299,399,499]
was=list(map(lambda a:a+1,lst2))
print(was)
