#Adding a number at Front and end:
n=int(input())  #main number
x=int(input())   #adding a number front and end
n=(n*10)+x
reverse=0
while (n>0):
    r=n%10
    reverse=(reverse*10)+r
    n=n//10
reverse=(reverse*10)+x
reverse1=0
while (reverse>0):
    r=reverse%10
    reverse1=(reverse1*10)+r
    reverse=reverse//10
print(reverse1)
    
