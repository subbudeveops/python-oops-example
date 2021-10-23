#enumerate(): we can list of all cu active thread currently running .  a list of current excutive threads you are going to get once list of current exuctive thread then if u want u can able to print thread information(name, identification,active_count,isalive)
from threading import *
import time
def display():
    print(current_thread().name,'...started')
    time.sleep(3)
    print(current_thread().name,'...ended')
print('current active thread:',active_count())
t1=Thread(target=display,name='child thread-1')
t2=Thread(target=display,name='child thread-2')
t3=Thread(target=display,name='child thread-3')
t1.start()
t2.start()
t3.start()
l=enumerate()
for t in l:
    print('Thread name:',t.name)
    print('Thread Identifier:',t.ident)
    print('Thread IsAlive:',t.isAlive())
    print()
time.sleep(10)
l=enumerate()
for t in l:
    print('Thread name:',t.name)
    print('Thread Identifier:',t.ident)
    print()