#Multi therading
import threading
print('current thradig name:',threading.current_thread().getName())
# how many ways we can create own thread
# #3 ways is three ways is there 
# 1.creating thread without using class
#2.creating thread with extend thread class
#3.creating thread eith out extend thread class
from threading import *
def display():
    for i in range(10):
        print('child Thread')
t=Thread(target=display)# Creating thread object to excute
t.start()
for i in range(10):
    print('main thread')
print()

#2.creating thread with extend Thread class
from threading import *
class mythread(Thread):
    def run(self):
        for i in range(5):
            print('child thred-1')
t=mythread()
t.start()
for i in range(5):
    print('main Thread-1')

print()
#3.creating thread with out extend thread class
from threading import *
class Test:
    def m1(self):
        for i in range(5):
            print('Child Thread')

obj=Test()
t=Thread(target=obj.m1)
t.start()
for i in range(10):
    print('main thread')


