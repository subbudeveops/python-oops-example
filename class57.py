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
#EX:
import re
count=0
pattern=re.compile('python')
matcher=pattern.finditer('i learn python very esay')
for match in matcher:
    print('match isvavailble at start index:',match.start())
    count=+1
print('number os occurance:',count)
