#1.Write a python program to find out common letter between two strings
'''
str1="reene"
str2="naina"
s1=set(str1)
s2=set(str2)
lst=(s1& s2)
print(lst)

#2.Write a python program to count a frequency of words in given input
T= int(input())
string=input().split()
d={}
for i in string:
    if i not in d.keys():
        d[i]=0
    d[i]=d[i]+1
print(d)

#3.Write a python program to convert list into a dictionary
keys=[1,2,3]
values=["akki","ajji","lachhi"]
res=dict(zip(keys,values))
print(res)
'''
#4. Findout the missing number in an given array
array=[1,2,3,5,6,7]
n=array[-1]
total=(n*(n+1))//2
summation=sum(array)
b=total-summation
print(b)
#5.find out pairs with given sum value of an array

array = [5, 7, 4, 3, 9, 8, 19, 21]
sum_value = 17
d = {}
for i in range(len(array)):
    num = array[i]
    difference = sum_value - num
    
    if difference in d:
        print(difference,num)
    d[num] = i

#6.remove the duplicates from the sorted list

sorted_list = [1, 4, 4, 5, 5, 12,45,45,12, 7, 8, 8, 9]

unique_list = []


for i in range(len(sorted_list)):
    if i == 0 or sorted_list[i] != sorted_list[i - 1]:
        unique_list.append(sorted_list[i])
print(unique_list)

