a=int(input())
b=int(input())
c=int(input())
if a>b and a>c:
    a=0
elif b>a and b>c:
    b=0
else:
    c=0
if a>b and a>c:
    print(a)
elif b>a and b>c:
    print(b)
else:
    print(c)
