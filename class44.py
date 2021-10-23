#muti threading
#is_alive(): how to know Thread is alive or not we can use this method is_alive()
from threading import *
import time
def display():
    print(current_thread().name,'...started')
    time.sleep(3)
    print(current_thread().name,'...ended')
print('current active thread:',active_count())
t1=Thread(target=display,name='child thread-1')
t2=Thread(target=display,name='child thread-2')
t1.start()
t2.start()
print('is Alive:',t1.is_alive())
print('is Alive:',t2.is_alive())
time.sleep(10)
print('is Alive:',t1.is_alive())
print('is Alive:',t2.is_alive())