# Problems on string     #aabcccccaaa (input)       a2b1c5a3(output)
#1. compress a string
s=input()
res=" "
c=1
n=len(s)
for i in range(1,n):
    if s[i]==s[i-1]:
        c = c + 1
    else:
        res = res +s[i-1] + str(c)
        c = 1
res = res + s[-1] + str(c)
print(res)
'''
#2.Vowels in a string
s= input()
res="aeiouAEIOU"
for i in s:
    if i  not in res:
        print("NO")
        break
    else:
        print("YES")
        break
        
#3.count Vowles and Consonants
s=input()
x="aeiouAEIOU"
vc=cc=0
for i in s:
    if i.isalpha():
        if i in x:
            vc=vc+1
        else:
            cc=cc+1
print(vc,cc)       
'''
