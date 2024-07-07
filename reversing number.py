# Reverse of the Number:
number=int(input())
reverse=0
if(number >= 0):
    while number > 0:
        r=number % 10
        reverse=(reverse*10)+r
        number=number // 10
    print(reverse)
else:
    number=-1 * number
    while number > 0:
        r=number % 10
        reverse=(reverse*10)+r
        number=number // 10
    print(-1*reverse)

