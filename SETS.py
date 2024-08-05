#Creation of sets
'''
s=set() #creation of empty set
print(s)
print(type(s))
s1={1,2,3,4,5}
print(s1)
s2={1,2,4,1,2,4,8}
print(s2)
s3={5,6,2.3,"python","akki"}
print(s3)
s4=set([4,5,2,1,2,5,4])
print(s4)
print(type(s4))
s5=set(map(int,input().split()))
print(s5)
print(type(s5))
#Accessing of sets
# there is only one method is For loop:
s6={4,2,3,56.36,9,56}
for i in s6:
    print(i)
'''
#SET METHODS:
'''
s1={1,2,3,45,8,1,2}
print(s1)
#Add
s1.add(13)
print(s1)
#update()
s2={1,2,3,4,5,7}
s3={2,5,6,8,1,4,5}
print(s2)   #before updating
print(s3)   #before updating
s2.update(s3) 
print(s2)  # after updating 
print(s3)  # it remains same as intial declared 
s3.update(s2)
print(s3)  # after updating

#copy
s={2,3,5,8,9,3,5,2,10,15}
print(s.copy())
#clear
s.clear()
print(s)
#remove
s={2,3,5,8,9,3,5,2,10,15}
s.remove(10)
print(s)
s.remove(20)
print(s)  # its shows an error called KeyError
#discard
s5={2,3,5,8,9,3,5,2,10,15}
s5.discard(9)
print(s5)
s5.discard(14)
print(s5) # if it is not avilable in the set it will out of operations and gives the output
#pop
s6={2,3,5,8,9,3,5,2,10,15}
s6.pop()
print(s6)
'''
#union
s2={1,2,3,4,5,7}
s3={2,5,6,8,1,4,5}
print(s2)
print(s3)
print(s2.union(s3))
#Intersection
s4={1,2,3,4,5,7}
s5={2,5,6,8,1,4,5}
print(s4.intersection(s5))
#intersection_update
s6={1,2,3,4,5,7}
s7={2,5,6,8,1,4,5}
s6.intersection_update(s7)
print(s6) #here s6 will be updated and s7 will remains same as intial declared
print(s7)
#difference
s8={1,2,3,4,5,7}
s9={2,5,6,8,1,4,5}
print(s9-s8)
#difference_update
s10={1,2,3,4,5,7}
s11={2,5,6,8,1,4,5}
s11.difference_update(s10)
print(s10)
print(s11)
#symmetric_difference
s12={1,2,3,4,5,7}
s13={2,5,6,8,1,4,5}
print(s12.symmetric_difference(s13))
#symmeteric_difference_update
s14={1,2,3,4,5,7}
s15={2,5,6,8,1,4,5}
s14.symmetric_difference_update(s15)
print(s14)
print(s15)
#isdisjoint
ss={5,6,4,7,21,36,47,96}
ss1={9,3,8,12,78,29,14,26}
print(ss)
print(ss.isdisjoint(ss1))
#issubset
ss={1,2,3,7}
ss1={1,2,3,5,7,8}
print(ss.issubset(ss1))
#issuperset
ss={1,2,3,7}
ss1={1,2,3,5,7,8}
print(ss1.issuperset(ss))





























