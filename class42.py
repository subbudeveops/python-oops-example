#multi threading
#active_count:currently how many thread active or how many thread live
from threading import *
import time
def display():
    print(current_thread().name,'...started')
    time.sleep(3)
    print(current_thread().name,'...ended')
print('the number of active Thread:',active_count())
t1=Thread(target=display,name='child thread-1')
t2=Thread(target=display,name='child thread-2')
t3=Thread(target=display,name='child thread-3')
t1.start()
t2.start()
t3.start()
print('the number of active Thread:',active_count())
time.sleep(10)
print('the number of active Thread:',active_count())