#multi threading
#Daemon Thread
#Note: Main thread always non Daemon only
from threading import *
mt=current_thread()
print(mt.isDaemon())
print(mt.daemon)
print()
#how to change Daemon thread nauter 
#we can use t.setDaemon(true)
# note :If u want change Daemon natur before starting thread only u can able change Daemon nature once started we cant changes Daemon nature
#Note:main thread always non Daemon all reaming thread deamon nature inherited from parent
# note:parent thread non daemon then child thread also non Daemon
#note: Parent thread is deamon then child thread is also daemon
from threading import *
def job():
    print('excuted by child thread')
t=Thread(target=job)
print(t.isDaemon())
t.setDaemon(True)
print(t.isDaemon())
print()
#note: only main  thread non daemon reaming threads inheritance nature we can change daemon nature for reaming threads 
# eaxmple:
from threading import *
import time
def job1():
    print('excuted by t1')
    t2=Thread(target=job2)
    print('t2 is daemon:',t2.daemon)
    t2.start()
def job2():
    print('excuted by t2')
t1=Thread(target=job1)
t1.setDaemon(True)
print('t1 is Daemon:',t1.daemon)
t1.start()

