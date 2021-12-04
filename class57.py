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
l=re.findall('\W','a7@$b9k2')
print(l)

print()

#finditer():it return iterator of matched object
import re
match=re.finditer('\d','12@567d')
for m in match:
    print(m.start(),m.end(),m.group())

print()

#sub(): sub means subtitution or replacements
#re.sub(regex,replacement,targetstring)
import re
s=re.sub('\d','***','a7b8@9efg')
print(s)

print()

#subn():it as exactly same as sub exception  it alos returns the number of replacement
# this function is return tuple where element is result string and second element is number of replacement
#  t(resultsting,nuber of replacement)
import re
t=re.subn('\d','***','a@5b7')
print('the result string:',t[0])
print('nuber of replacement:',t[1])

print()

#split():if we want to spilt given target string according to a particular pattern then can go for spilt()
# this spilt si return list of all token
import re
s=re.split('-','10-20-30-40')
print(s)  

#. is regular expresion cosider all  that way \. or [.] is regular expression trated as symbols only
import re
l=re.split('[.]','www.subbu@gmail.com')
for s in l:
    print(s)

print()
#^symbol:we can use ^ symbol to check wheter the given target string start with our provided pattern or not
# ex:
# res=re.search('^Learn','s')
#if the target stirng start with Learn then it will return match object,other wise return None
import re
s='Learning python very easy'
res=re.search('^Learn',s)
if res!=None:
    print("target string start with Learn")
else:
    print('targer string not start with Learn')
print()
# $symbol:we can use $ symbol to check wheter the target string end with our provide pattern or not
# eg:res=re.search('Easy$',s)
# if the target string is end with Easy it will return match object,other wise return None 
import re
s="Learn with python is very Easy"
res=re.search('Easy$',s)
if res!=None:
    print('the target string is end with Easy')
else:
    print('target string end not with Easy')
print()
#Note:if we want ignore case then we have to pass 3rd argument re.IGNORECASE for search() function
import re
s="Learn with python is very easy"
res=re.search('Easy$',s,re.IGNORECASE)
if res!=None:
    print('the target string is end with Easy')
else:
    print('target string end not with Easy')

    print()

#App:To write a python program to extract all mobile numbers present in input.txt where number are mixed with normal text data
import re
f1=open('input.txt','r')
f2=open('output.txt','w')
for line in f1:
    list=re.findall('[7-9]\d{9}',line)
    for n in list:
        f2.write(n+"\n")
print("Extract all nuber into output.txt ")
f1.close()
f2.close()


print()

#Example of Regular Expression
#1.first chsrcter should be lower case from a to k
#2.the second character should be digits divisble by 3
#3.the length identifier shouble at least 2
import re
s=input('Enter the indentifier:')
res=re.fullmatch('[a-k][0369][a-zA-Z0-9#]*',s)
if res!=None:
    print(s,'is validate yava identifier')
else:
    print(s,'is not yava identifier')






