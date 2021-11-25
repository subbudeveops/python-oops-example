#Aliasing,Cloing,Deep copy and Shallow Copy
#Aliasing and Cloing
#EX:Aliasing happend whenever variable assigned to another variable
#ex a=10
#b=a
#b=10
l1=[1,2,3]
l2=l1
print(l2)#[1, 2, 3]
l1.append(4)
print(l2)#[1, 2, 3, 4]
print(l1 is l2)
print()
#cloning list:
#create copy of the original list
# the new list can be without changed  orginal list
#ex:
l1=[1,2,3]
l2=l1.copy()
#or
l2=l1[:]
print(l2)
print(l1 is l2)
l1.append(4)
print(l1)
print(l2)