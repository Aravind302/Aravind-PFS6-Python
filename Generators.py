#Generators
'''
def hello():
    for i in range(1,12):
        yield i
x=hello()
for i in x:
    print(i)
    '''
# next() in generators
def infinite_even():
    n = 0
    while True:
        yield n
        n += 2

a = infinite_even()

for i in range(10):
    print(next(n))
    
     

   
