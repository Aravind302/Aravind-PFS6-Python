# Regex Functions

#\d ( it will match any single digit in a string [0-9])
import re
'''
pattern = r'\d'
text= "the cost of pen is 3  rupees"
matches= re.findall(pattern,text)
print(matches)
'''
#/D ( it will match any character that is not a digit)
'''
pattern = r'\D'
text= "the cost of pen is 3 rupees"
matches= re.findall(pattern,text)
print(matches)
''' 
#\s (matches any white space character)
'''
pattern = r'\s'
text= "the cost of pen is 3 rupees"
matches= re.findall(pattern,text)
print(matches)
'''
#\S (matches any non-white space character)
'''
pattern = r'\S'
text= "the cost of pen is 3  rupees"
matches= re.findall(pattern,text)
print(matches)
'''
#\w(matches any word character [alphanumeric + underscores])
'''
pattern = r'\w'
text= "the cost of pen is 3 _ rupees"
matches= re.findall(pattern,text)
print(matches)
'''
#\W (matches any non-word character)[#:@$%^&*]
'''
pattern = r'\W'
text= "the cost of pen is 3  rupees:$"
matches= re.findall(pattern,text)
print(matches)
'''
#\A (it will match a word at the begining of the string)
'''
pattern=r'\Ahello'
text= "hello world i am aravind"
matches=re.findall(pattern,text)
print(matches)
'''
#\b ( it represents a word boundary)
'''
pattern=r'\bam'
text= "hello world i am aravind"
matches=re.findall(pattern,text)
print(matches)
'''
#\B ( it represents a non-word boundary)
'''
pattern=r'\Bo'
text= "hello world i am aravind"
matches=re.findall(pattern,text)
print(matches)
'''
#\Z (it will match a word at end of the string)
'''
pattern=r'aravind\Z'
text= "hello world i am aravind"
matches=re.findall(pattern,text)
print(matches)
'''
# Basic Meta Characters in Regex
# dot (.)
'''
pattern= r'h.t'
text="not,hot,haat,hap,sat"
matches=re.findall(pattern,text)
print(matches)
'''
#caret(^)
'''
pattern=r'^the'
text="the price is 23 rupees"
matches= re.findall(pattern,text)
print(matches)
'''
#dollar($)
'''
pattern=r'rupees$'
text="the price is 23 rupees"
matches= re.findall(pattern,text)
print(matches)
'''
#Asterick (*)
'''
pattern=r'ab*c'
text="abc,abbc,abbd,abb,acc"
matches= re.findall(pattern,text)
print(matches)
'''
#plus(+)
'''
pattern=r'ab+c'
text="abc,abbc,abbd,abb,acc"
matches= re.findall(pattern,text)
print(matches)

'''
#question mark (?)
'''
pattern=r'abc?'
text="abc,abbc,abbd,abb,acc"
matches= re.findall(pattern,text)
print(matches)
'''

# curly braces{}
'''
pattern=r'\d{4}-\d{2}-\d{2}'
text="the  today date is 2024-07-30"
matches= re.findall(pattern,text)
print(matches)
'''

#set brackets[]
'''
pattern=r'[ch]at'
text="the cat wears hat"
matches= re.findall(pattern,text)
print(matches)
'''

#pipe(|)
'''
pattern=r'cat|hat'
text="the cat wears hat"
matches= re.findall(pattern,text)
print(matches)

'''























































