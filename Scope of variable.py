#Global Variable (it can be accessed throughout the program body)

x = 10
def fun():
    print(x)
print(x)
fun()

#Local Variable (it can be accessed only inside the function in which they are declared)
def fun():
    x = 10
    print(x)
fun()

#Local and Global

x = 10
def fun():
    y = 20
    print(x)
    print(y)
fun()
print(x)
