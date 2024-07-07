# Decomposition of a Number
n=int(input())
res=0
if n>=0:
    while(n>0):
          r=n%10
          res=(res*10)+r
          n=n//10
    while res>0:
        r=res%10
        print(r)
        res=res//10
else:
    n=-1*n
    while(n>0):
          r=n%0
          res=(res*10)+r
          n=n//10
    while res>0:
        r=res%10
        print(r)
        res=res//10
#upcoming even number:
n=int(input())
if n%2 == 0:
    print(n+2)
else:
    print(n+1)
