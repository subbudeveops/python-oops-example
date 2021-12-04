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