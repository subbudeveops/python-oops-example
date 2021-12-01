#Regular Expression
#if u want to represent group of string according to particular pattern then we should go for regular expression
#main important applications area of Regular expression:
#--------------------------------------------------------
#1.validation
#2.pattern matching  ex:ctrl f,
#3.to develop tranlater like compiler,interpreters,assembles
#4.to develop digital circuits
#5.to develop communication protocols tcp/ip etc
#we can develop Regular expression based application by using module:re
# this module contain several inbuilt functions
# 1.compile()function:
# ex:i want to search 'python in given string first step is 
# 1.python we can convert to Regex object 
#pattern=re.compile('python)
import re
pattern=re.compile('python')
#2.finditer()
#matcher=pattern.finditer('i learn python is so esay pathan')
#inside finditer 3steps is there
#1.start()=start index of the match
#2.end()=end+1 index of the match
#3.group()=return match string
#EX:
import re
count=0
pattern=re.compile('ab')
matcher=pattern.finditer('abbbabcbabab')
for match in matcher:
    
    print('match isvavailble at start index:',match.start())
    count+=1
    
print('number os occurance:',count)
print()

import re
count=0
pattern=re.compile('ba')
match=pattern.finditer('abaababa')
for m in match:
    print('start:{},end:{},group:{}'.format(m.start(),m.end(),m.group()))
    count+=1
#print('total occurance:',count)
print()
#or without compiler example directly use finditer
import re
match=re.finditer('ab','abaababa')
for m in match:
    print('start:{},end:{},group:{}'.format(m.start(),m.end(),m.group()))
    count+=1
print('total occurance:',count)
#charater class
#--------------
#[abc]=either a or b or c
#[^abc]=accept abc
#[a-z]=only lower case alphabet syambols
#[A-Z]=only upper case alphabet symbols
#[a-zA-z]=any alphabet symbol
#[0-9]
#[0-9a-zA-Z]
#[^a-zA-Z0-9]

import re
matcher=re.finditer('[abc]','a@7bk9z')
for m in matcher:
    print(m.start(),'....',m.group())
print()
#predefined character class:
#---------------------------
# \s=space character
# \S= accept space character
# \d= any digits or[0-9]
#\D= accept any digits or[^0-9]
#\w = any word character(alpha numeric character) or [a-zA-z0-9]
#\W = any character except word or[^a-zA-Z0-9]
# .==Every character
import re
matcher=re.finditer('.','a@7 bk9z')
for m in matcher:
    print(m.start(),'....',m.group())

print()

# Quantifiers:
#------------
#a=where a is  extaly one a
#a+=atleast one a
#a*=any number of a including zero number
#a?=atmost one a either one a or zero number of a's
#a{n}=Exatly n number od a's
#a{m,n}= minimum number os a's and maximum n number of a's
#[^a]=accept a remaing
# ^a=it will check given target string  start with a or not
# a$= it will check given target string ends with a or not
#example
import re
matcher=re.finditer('a{2,3}','abaabaaab')
for m in matcher:
    print(m.start(),'......',m.group())

print()

#important function of re module:
#-----------------------------------
#1.match():we can use this function to check the given pattern at begining of the target string if then return match object otherwise None
#Ex:
import re
s=input('Enter pattern to check:')
m=re.match(s,'abcdefg')
if m!=None:
    print('match is availableat the begining of the string')
    print('starting index:{} ending index:{}'.format(m.start(),m.end()))
else:
    print("match is not available the begining of the string")

print()

#2.fullmatch():we can use this function to check the pattern at full of the target string 
import re
s=input('Enter pattern to check:')
m=re.fullmatch(s,'abcdefg')
if m!=None:
    print('fullmatch is availableat  of the string')
    print('starting index:{} ending index:{}'.format(m.start(),m.end()))
else:
    print("fullmatch is not available  of the string")

print()

#search():to search the given pattern in target  string . if return match object of the occurance otherwise none
import re
s=input('Enter pattern to check:')
m=re.search(s,'abaaabcdefg')
if m!=None:
    print('match is availabe')
    print('first occurance with start index:{} ending index:{}'.format(m.start(),m.end()))
else:
    print("full string is not matched")

print()

#findall():can u find all the match and return the list

import re
l=re.findall('[0-9]','a7b9k2')
print(l)

