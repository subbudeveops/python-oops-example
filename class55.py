#Shallow  copy and Deep copy
#Shallow copy:
# If the Original Object  contain any reference to mutable object ,just duplicate reference variable will be created
#pointing to old contened object,but not buplicate objectin creation
import copy
l1=[10,20,[30,40],50]
l2=copy.copy(l1)
l1[0]=111
l1[1]=222
l1[2][0]=888
l1[2][1]=999
l1[3]=777
print('l1:',l1)
print('l2:',l2)
print()
#here we cant copy original data override the 
# Deep copy
import copy
l1=[10,20,[30,40],50]
l2=copy.deepcopy(l1)
l1[0]=111
l1[1]=222
l1[2][0]=888
l1[2][1]=999
l1[3]=777
print('l1:',l1)
print('l2:',l2)
#note:If original object does not contain nested object then we should go for shallow cloning
#if Original object contain any nested object then we should go for deep cloning

