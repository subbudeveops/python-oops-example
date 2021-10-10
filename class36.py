#data hiding
#we are using double underscore (__) before the attribute or variable nas those variable hide to the other class 
#Ex:__a=10 private variable
# same like private variable

class A:
    def __init__(self,a,b,c):
        self.a=a
        self._b=b
        self.__c=c
    def display(self):
        print(self.a)#public variable
        print(self._b)#protected variable
        print(self.__c)#private variable
class B(A):
    def __init__(self,a,b,c,d):
        super().__init__(a,b,c)
        self.d=d
    def display(self):
        super().display()
        print(self.d)
b=B(10,20,30,40)
b.display()

print()

#data hiding example
class Solution:
    __privatecounter=0
    def sum(self):
        self.__privatecounter+=1
        print(self.__privatecounter)
count=Solution()
count.sum()
count.sum()
count.sum()
#print(count.__privatecounter)#we cant acess private variable
print(count._Solution__privatecounter)#accesing private variable





