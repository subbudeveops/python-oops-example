#muti threading
#synchronization by using Locks
#ex:as per below example if person1 accuping room-1 but same time preson2 also accuing room-1 that way
#person-1 is accuping room-1 until unless person-1 vaacating room-1 after then only person-2 accuping room-1 
#that way we are using lock()
from threading import *
import threading
import time
def person1(lock):
    lock.acquire()
    print('person-1 is accuting Room-1')
    time.sleep(3)
    print('person-1 is vaccting Room-1')
    lock.release()

def person2(lock):
    lock.acquire()
    print('person-2 is accuting Room-1')
    time.sleep(3)
    print('person-2 is vaccting Room-1')
    lock.release()

lock=threading.Lock()
t1=Thread(target=person1,args=(lock,))
t2=Thread(target=person2,args=(lock,))
t1.start()
t2.start()



