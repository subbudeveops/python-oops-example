#Debbuging by using Assertion
#Exception handling
#Assertion can be used to performing debbuging
#Debbuging purposes
#Process of Identifing and fixing the bug is called Debbuging
# How we can perform debbuing
#ans:most people alway using of print()
#but this print() should be removed after fixing debbuging other wise clint side printing the print() statement problem that we can use assert statement we cant delete this assert 
#type of assert  statements
#1.simple version
#2.very simple version(Argumented Version)
#1.simple version:
#assert condition_expression
#Ex:
x=10
assert x==10   
print(10)
#2.Argument version
#assert condition_expression,message
x=10
assert x==10,'here should x value >10 it is not'
print(x)
#output
#  File "class56.py", line 21, in <module>
#assert x>10,'here should x value >10 it is not'
#AssertionError: here should x value >10 it is not
print()
def squareIt(x):
    return x**x
print(squareIt(2))
print(squareIt(3))
print(squareIt(4))
#output:
#4
#27
#256
print()
#how to dont print assert statement on console we can use 
#pyhton -O class56.py

#ex:
def squareIt(x):
    return x**x    # here mistake because single * only but double star is there
assert squareIt(2)==4,'The squre of 2 should be 4'
assert squareIt(3)==9,'The squre of 3 should be 9'
assert squareIt(4)==16,'The squre of 4 should be 16'
print(squareIt(2))
print(squareIt(3))
print(squareIt(4))
#OUTPUT:
# Traceback (most recent call last):
#File "class56.py", line 36, in <module>
# assert squareIt(3)==9,'The squre of 3 should be 9'
#AssertionError: The squre of 3 should be 9
 print()


def squareIt(x):
    return x**x    # here mistake because single * only but double star is there
assert squareIt(2)==4,'The squre of 2 should be 4'
assert squareIt(3)==9,'The squre of 3 should be 9'
assert squareIt(4)==16,'The squre of 4 should be 16'
print(squareIt(2))
print(squareIt(3))
print(squareIt(4))

#i dont want assert message i want output
#output
#python -O class56.py
#4
#27
#256
print()
def squareIt(x):
    return x*x    # here mistake because single * only but double star is there
assert squareIt(2)==4,'The squre of 2 should be 4'
assert squareIt(3)==9,'The squre of 3 should be 9'
assert squareIt(4)==16,'The squre of 4 should be 16'
print(squareIt(2))
print(squareIt(3))
print(squareIt(4))

#output
#4
#9
#16
#complte store about assert concept