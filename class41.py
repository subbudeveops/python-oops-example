#example of multi threading and without multi threading
#ex:with multi threading
from threading import *
import time
def double(numbers):
    for n in numbers:
        time.sleep(3)
        print('double value:',2*n)
 
def square(numbers):
    for n in numbers:
        time.sleep(3)
        print('square value:',n*n)
numbers=[1,2,3,4,5]
begintime=time.time()
t1=Thread(target=double,args=(numbers,))
t2=Thread(target=square,args=(numbers,))
t1.start()
t2.start()
t1.join()
t2.join()
endtime=time.time()
print('the total time taken:',endtime-begintime)
